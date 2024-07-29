import joblib
from utils.code_files.common_utils import read_params,get_data
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV, KFold
from sklearn.preprocessing import MinMaxScaler, RobustScaler,StandardScaler
from sklearn.linear_model import LinearRegression, Lasso, Ridge
from sklearn.ensemble import GradientBoostingRegressor, AdaBoostRegressor, RandomForestRegressor
from xgboost import XGBRegressor
from catboost import CatBoostRegressor
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
import mlflow
import mlflow.sklearn
from argparse import ArgumentParser
from utils.code_files import common_utils
import logging
from datetime import datetime
from utils.code_files.ml_utils.plot_residuals import plot_residuals
from utils.code_files.ml_utils.plot_feature_importances import plot_feature_importances
logger = logging.getLogger(__name__)



def best_model(model_data,configs):
    best_model_path=configs['model_training']['best_model']
    object_loc_prefix=configs['model_training']['object_loc_prefix']   
    residual_loc=configs['model_training']['residual_plot']
    feature_importance_loc=configs['model_training']['feature_importance']
    scaler_x_loc=configs['model_training']['scaler_x']
    scaler_y_loc=configs['model_training']['scaler_y']
    model_data=model_data.sample(frac=0.2).reset_index(drop=True)
    X = model_data.drop(columns=['Listed_Price'],axis=1)
    y = model_data['Listed_Price']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    scalers = {
        'RobustScaler': MinMaxScaler()
    }
    models = {
        'Linear Regression': {
            'model': LinearRegression(),
            'params': {
                'fit_intercept': [True, False]
            }
        },
        'Random Forest': {
            'model': RandomForestRegressor(),
            'params': {
                'n_estimators': [50,100,150],
                'max_depth': [None, 5,6,10,15,20],
                'min_samples_split': [2, 5, 10]
            }
        },
        'Adaboost':{
            'model': AdaBoostRegressor(),
            'params':{
                    'n_estimators': [50, 100, 150],
                    'learning_rate': [0.01, 0.1, 0.5],
                    'loss': ['linear', 'square', 'exponential']
            }
        },
        'GradientBoostingRegressor':{
            'model': GradientBoostingRegressor(),
            'params':{
                    'n_estimators': [50, 100, 200],
                    'learning_rate': [0.01, 0.1, 0.2],
                    'max_depth': [3, 4, 5],
                    'min_samples_split': [2, 5, 10],
                    'min_samples_leaf': [1, 2, 4],
                    'subsample': [0.8, 0.9, 1.0]
                }
        },
        
        'Ridge': {
            'model': Ridge(),
            'params': {
                'alpha': [0.1, 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
            }
        },
        'XGBoost':{
            'model': XGBRegressor(),
            'params':{
                'n_estimators': [50, 100, 200],
                'learning_rate': [0.01, 0.1, 0.2],
                'max_depth': [3, 6, 9],
                'subsample': [0.8, 0.9, 1.0],
                'colsample_bytree': [0.8, 0.9, 1.0],
                'gamma': [0, 0.1, 0.2],
                'reg_alpha': [0, 0.1, 1],
                'reg_lambda': [1, 1.5, 2]}
        },
        
    }
    
    best_models = []
    # Start MLflow experiment
    mlflow.set_tracking_uri('artifacts/mlruns')
    mlflow.set_experiment('Used Car Price Prediction')
    for scaler_name, scaler in scalers.items():
        scaler_X = scaler
        X_train_scaled = scaler_X.fit_transform(X_train)
        X_test_scaled = scaler_X.transform(X_test)

        scaler_y = scaler
        y_train_scaled = scaler_y.fit_transform(y_train.values.reshape(-1, 1)).flatten()
      
        kf = KFold(n_splits=5, shuffle=True, random_state=42)
        for model_name, config in models.items():
            logger.info(f"Started Training Model: {model_name}")
            run_name=model_name+" "+str(datetime.now())
            with mlflow.start_run(run_name=run_name):
                    try:
                        mlflow.log_param('scaler', scaler_name)
                        grid_search = GridSearchCV(config['model'], config['params'], cv=kf, scoring='r2', n_jobs=-1)
                        grid_search.fit(X_train_scaled, y_train_scaled)
                        
                        best_model = grid_search.best_estimator_
                        best_params = grid_search.best_params_
                        best_score = grid_search.best_score_
                        
                        # Predicting and inverse transforming the predictions
                        y_pred_scaled = best_model.predict(X_test_scaled)
                        y_pred = scaler_y.inverse_transform(y_pred_scaled.reshape(-1, 1)).flatten()
                        
                        # Evaluate the model
                        r2 = r2_score(y_test, y_pred)
                        mse = mean_squared_error(y_test, y_pred)
                        mae = mean_absolute_error(y_test, y_pred)
                        print(f'Model {model_name}, best r2_score: {r2}')
                        # Log parameters and metrics
                        mlflow.log_params(best_params)
                        mlflow.log_metric('train_r2', best_score)
                        mlflow.log_metric('test_r2', r2)
                        mlflow.log_metric('test_mse', mse)
                        mlflow.log_metric('test_mae', mae)
                        
                        # Log the model
                        mlflow.sklearn.log_model(best_model, model_name)
                        plot_residuals(y_test, y_pred, model_name)
                        mlflow.log_artifact(f'{object_loc_prefix}{model_name}{residual_loc}')
                        
                        if hasattr(best_model, 'feature_importances_'):
                            feature_importances = best_model.feature_importances_
                            features = X.columns
                            plot_feature_importances(feature_importances, features, model_name)

                            mlflow.log_artifact(f'{object_loc_prefix}{model_name}{feature_importance_loc}')
                        
                        
                        best_models.append({
                            'model_name': model_name,
                            'model': best_model,
                            'params': best_params,
                            'r2': r2,
                            'mse': mse,
                            'mae': mae
                        })
                        logging.info(f"{model_name} Trained with R2 of {r2}, mse of {mse}, mae of {mae}")
                    except Exception as e:
                        raise e
        #Log Scaler
        joblib.dump(scaler_X,scaler_x_loc)
        joblib.dump(scaler_y,scaler_y_loc)
        mlflow.log_artifact(scaler_x_loc)
        mlflow.log_artifact(scaler_y_loc)        

    # Find the best model based on test R2 score
    best_model_info = max(best_models, key=lambda x: x['r2'])
    joblib.dump(best_model_info['model'], best_model_path)
    return best_model_info,best_model_path
    

if __name__=="__main__":
    args=ArgumentParser()
    args.add_argument('--config_path','-c',default='params.yaml')
    parsed_args=args.parse_args()
    config_path=parsed_args.config_path
    configs=read_params(config_path)


    logging.info("Beginning Model Training")
    try:
        model_data=get_data(configs,"model_training")
        best_model_info,best_model_path=best_model(model_data,configs)
        logging.info(f"Best Model: {best_model_info['model_name']} with R2: {best_model_info['r2']}")
        logging.info(f"Best Model Stored in Location {best_model_path}")
    except:
        logging.error("Model Training Failed",exc_info=True)
