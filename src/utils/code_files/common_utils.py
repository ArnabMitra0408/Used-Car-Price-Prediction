#importing libraries
import numpy as np
import os
import pandas as pd
import yaml
import zipfile
import logging
import mysql.connector
from mysql.connector import Error

class sql_connect:
    def __init__(self):
        try:
            self.connection = mysql.connector.connect(
                host='localhost',
                database='carpricepipelinelogs',
                user='root',
                password='root'
            )
            if self.connection.is_connected():
                self.cursor = self.connection.cursor()
                print("Connected to MySQL database")
        except Error as e:
            print(f"Cannot Connect to DB {e}")
            self.connection = None

    def execute_query(self, query, params=None):
        try:
            if self.connection is not None:
                if params:
                    self.cursor.execute(query, params)
                else:
                    self.cursor.execute(query)
                self.connection.commit()
                print(f"Query executed: {query}")
            else:
                print("No database connection.")
        except Error as e:
            print(f"Failed to execute query: {e}")

    def close_connection(self):
        if self.connection is not None and self.connection.is_connected():
            self.cursor.close()
            self.connection.close()
            print("MySQL connection is closed")


class Custom_Handler(logging.Handler):
    def __init__(self, db):
        super().__init__()
        self.db = db

    def emit(self, record):
        try:
            if record:
                query = """
                    INSERT INTO LOGS (LevelName, Message, DateCreated) 
                    VALUES (%s, %s, SYSDATE())
                """
                params = (record.levelname, record.msg)
                self.db.execute_query(query, params)
        except Exception as e:
            print(f"Failed to log message to database: {e}")


db = sql_connect()
custom_handler = Custom_Handler(db)
logger = logging.getLogger('Pipeline')
logger.setLevel(logging.DEBUG)
logger.addHandler(custom_handler)


def clean_dir(dir_path:str)-> None:
    #Removes all the files in a directory. 
    if len(os.listdir(dir_path)) == 0:
        logger.info(f'directory {dir_path} already empty')
    else:
        for root, dirs, files in os.walk(dir_path):
            for file in files:
                file_path = os.path.join(root, file)
                os.remove(file_path)
        logger.info(f'directory {dir_path} cleaned')

def create_dir(paths:list) -> None:
    for path in paths:
        if os.path.exists(path):
            logger.info(f'directory {path} already exists')
        else:
            os.mkdir(path)
            logger.info(f'directory {path} created')


def unzip_file(zip_filepath, extract_to):
    try:
        with zipfile.ZipFile(zip_filepath, 'r') as zip_ref:
            zip_ref.extractall(extract_to)
        logger.info(f'Zip File Extracted to path {extract_to}')
    except:
        logger.error(f'Zip File Could Not Be Extracted',exc_info=True)


def read_params(config_path:str) -> dict:
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config

def save_df(df,loc):
    try:
        df.to_csv(loc,index=False)
        print(f"Dataframe saved: {loc}")
    except Exception as e:
        raise e
    
def converst_to_number(x, conv: str = 'float'):
    x = str(x)
    new_str = ''
    is_dec = True
    for a in x:
        if 48 <= ord(a) <= 57:
            new_str += a
            continue
        elif a == ',' or a == '_':
            continue
        elif a == '.' and is_dec:
            new_str += a
            is_dec = False
        else:
            break
    
    if new_str == '':
        return None
    
    if conv == 'int':
        return int(new_str)
    
    return float(new_str)

def get_begin_number(x):
    return converst_to_number(x, 'int')

def get_begin_float(x):
    return converst_to_number(x, 'float')



def get_data(configs,pipeline_step):
    if pipeline_step=='processing':
        model_data_loc=configs['data_dir']['cars_data_clean']
        model_data=pd.read_csv(model_data_loc)
        return model_data
    elif pipeline_step=='model_training':
        model_data_loc=configs['data_dir']['cars_data_final']
        model_data=pd.read_csv(model_data_loc)
        return model_data
