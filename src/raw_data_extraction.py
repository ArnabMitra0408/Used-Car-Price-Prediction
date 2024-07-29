#importing Libraries
import pandas as pd
from argparse import ArgumentParser
import logging
from utils.code_files import common_utils
from utils.code_files.common_utils import read_params,unzip_file,clean_dir,create_dir
logger = logging.getLogger(__name__)

def extract_data(config_path):
    # Function to extract raw data and put in the appropriate directory
    configs=read_params(config_path)
    zip_data=configs['data_dir']['raw_zip_data']
    csv_data_dir=configs['data_dir']['raw_csv_data_dir']
    create_dir([csv_data_dir])
    clean_dir(csv_data_dir)
    unzip_file(zip_data,csv_data_dir)
 
if __name__=="__main__":
    args=ArgumentParser()
    args.add_argument("--config_path", '-c', default='params.yaml')
    logging.info("Raw Data Extraction Started")
    parsed_args=args.parse_args()

    try:
        extract_data(parsed_args.config_path)
        logging.info("Raw Data Extraction Successful")
        
    except Exception as e:
        logging.error("Raw Data Extraction Failed",exc_info=True)
