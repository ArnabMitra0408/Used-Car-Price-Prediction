import mlflow
from mlflow.tracking import MlflowClient
import mlflow.pyfunc
from argparse import ArgumentParser
import pickle
from utils.code_files import common_utils
from utils.code_files.common_utils import read_params
from utils.code_files.common_utils import sql_connect,Custom_Handler
import logging
db = sql_connect()
custom_handler = Custom_Handler(db)
logger = logging.getLogger('Pipeline')
logger.setLevel(logging.DEBUG)
logger.addHandler(custom_handler)


def save_best_model(configs):
    best_model_path=configs['model_training']['best_model']
    artifacts_uri=configs['model_training']['artifacts_uri']
    mlflow.set_tracking_uri(artifacts_uri)
    experiments=mlflow.search_experiments()

    for experiment in experiments:
        if experiment.experiment_id==0 or experiment.experiment_id=='.trash':
            continue
        else: 
            runs = mlflow.search_runs(experiment_ids=[experiment.experiment_id])
            run_id = runs[runs['metrics.test_r2'] == runs['metrics.test_r2'].max()]['run_id'].values[0]
            run_name=runs[runs['metrics.test_r2'] == runs['metrics.test_r2'].max()]['tags.mlflow.runName'].values[0]
            print(run_name)
            model_name=''
            if 'Random Forest' in run_name:
                model_name='Random Forest'
            elif 'GradientBoostingRegressor' in run_name:
                model_name='GradientBoostingRegressor'
            elif 'XGBoost' in run_name:
                model_name='XGBoost'
            elif 'Linear Regression' in run_name:
                model_name='Linear Regression'
            elif 'Adaboost' in run_name:
                model_name='Adaboost'
            else: 
                model_name='Ridge'
            logger.info(f'Best Model is {model_name} with a Test R2 score of {runs['metrics.test_r2'].max()}')
            model_uri = f"{artifacts_uri}/{experiment.experiment_id}/{run_id}/artifacts/{model_name}/model.pkl"
            
            with open(model_uri, 'rb') as file:
                best_model = pickle.load(file)
            
            with open(best_model_path, 'wb') as file:
                pickle.dump(best_model, file)
            break
    logger.info(f"Model Saved in Location {best_model_path}")

if __name__=="__main__":
    args=ArgumentParser()
    args.add_argument('--config_path','-c',default='params.yaml')
    parsed_args=args.parse_args()
    config_path=parsed_args.config_path
    configs=read_params(config_path)
    

    logger.info("Beginning Saving Best Model")
    try:
        save_best_model(configs)
    except:
        logger.error("Model Saving Failed",exc_info=True)

    db.close_connection()