#Importing Libraries
import numpy as np
import pandas as pd
from utils.code_files.common_utils import read_params,save_df,get_data
from utils.code_files import common_utils
from argparse import ArgumentParser
from sklearn.preprocessing import OrdinalEncoder
import pickle

from utils.code_files.processing_utils.front_tread import front_tread
from utils.code_files.processing_utils.wheel_base import wheel_base
from utils.code_files.processing_utils.brake_type import brake_type
from utils.code_files.processing_utils.num_cylinder import num_cylinder
from utils.code_files.processing_utils.length import length
from utils.code_files.processing_utils.model import model
from utils.code_files.processing_utils.body_type import body_type
from utils.code_files.processing_utils.mileage import mileage
from utils.code_files.processing_utils.fuel_type import fuel_type
from utils.code_files.processing_utils.acceleration import acceleration
from utils.code_files.processing_utils.transmission_type import transmission_type
from utils.code_files.processing_utils.max_power_at import max_power_at
from utils.code_files.processing_utils.tyre_type import tyre_type
from utils.code_files.processing_utils.drive_type import drive_type
from utils.code_files.processing_utils.alloy_wheel_size import alloy_wheel_size
from utils.code_files.processing_utils.steering_type import steering_type
from utils.code_files.processing_utils.gear_type import gear_type
from utils.code_files.processing_utils.car_seller_type import car_seller_type
from utils.code_files.processing_utils.owner_type import owner_type
from utils.code_files.processing_utils.state import state
from utils.code_files.processing_utils.brand import brand
from utils.code_files.processing_utils.max_power_delivered import max_power_delivered
from utils.code_files.common_utils import sql_connect,Custom_Handler
import logging
db = sql_connect()
custom_handler = Custom_Handler(db)
logger = logging.getLogger('Pipeline')
logger.setLevel(logging.DEBUG)
logger.addHandler(custom_handler)



def processing(configs,clean_data):

    brand_config_path=configs['pickle_files']['brand_encoding']
    model_config_path=configs['pickle_files']['model_encoding']
    state_config_path=configs['pickle_files']['state_encoding']
    owner_type_config_path=configs['pickle_files']['owner_type_encoding']
    body_type_config_path=configs['pickle_files']['body_type_encoding']
    transmission_type_config_path=configs['pickle_files']['transmission_type_encoding']
    fuel_type_config_path=configs['pickle_files']['fuel_type_encoding']
    seller_type_config_path=configs['pickle_files']['seller_type_encoding']
    tyre_types_config_path=configs['pickle_files']['tyre_type_encoding']
    steering_type_config_path=configs['pickle_files']['steering_type_encoding']
    brake_type_config_path=configs['pickle_files']['brake_type_encoding']
    drive_type_config_path=configs['pickle_files']['drive_type_encoding']
    gear_box_config_path=configs['pickle_files']['gear_box_encoding']
    year_filter=configs['data_processing']['year_filter']
    
    try:
        clean_data = clean_data[clean_data['Manufactured_Year'] > year_filter]
        logger.info(f'Filetered Year Column to only take data after {year_filter}')
    except Exception as e:
        raise e

    try:
        clean_data=front_tread(clean_data)
        logger.info("Front Tread Column Processed")
    except Exception as e:
        raise e
    
    try:
        clean_data=max_power_at(clean_data)
        logger.info("Max Power At Column Processed")
    except Exception as e:
        raise e

    try:
        clean_data=max_power_delivered(clean_data)
        logger.info("Max Power Delivered Column Processed")
    except Exception as e:
        raise e
    
    try:
        clean_data=acceleration(clean_data)
        logger.info("Acceleration Column Processed")
    except Exception as e:
        raise e

    try:
        clean_data=length(clean_data)
        logger.info("length Column Processed")
    except Exception as e:
        raise e

    try:
        clean_data.dropna(subset=['Displacement'],inplace=True)
        logger.info("Displacement Column Processed")
    except Exception as e:
        raise e

    try:
        clean_data['KM_Driven']=clean_data['KM_Driven'].apply(np.log)
        logger.info("KM_Driven Column Processed")
    except Exception as e:
        raise e

    try:
        clean_data=num_cylinder(clean_data)
        logger.info("No of Cylinder Column Processed")
    except Exception as e:
        raise e
    
    try:
        clean_data=clean_data.reset_index(drop=True)
        clean_data=clean_data[clean_data['Seating Capacity']!=0]
        clean_data.dropna(subset='Seating Capacity',inplace=True)
        logger.info("Seating Capacity Column Processed")
    except Exception as e:
        raise e


    try:
        clean_data=clean_data.reset_index(drop=True)
        clean_data.dropna(subset='Num_Doors',inplace=True)
        logger.info("Num Doors column Processed")
    except Exception as e:
        raise e

    try:
        clean_data=alloy_wheel_size(clean_data)
        logger.info("Alloy Wheel Size Column Processed")
    except Exception as e:
        raise e

    try:
        clean_data.dropna(subset='Valves_Per_Cylinder',inplace=True)
        logger.info("Valves_Per_Cylinder Column Processed")
    except Exception as e:
        raise e
    
    try:
        clean_data=mileage(clean_data)
        logger.info("mileage Column Processed")
    except Exception as e:
        raise e


    try:
        clean_data=tyre_type(clean_data,tyre_types_config_path)
        logger.info("Tyre Type Processed")
    except Exception as e:
        raise e
     
    try:
        clean_data=transmission_type(clean_data,transmission_type_config_path)
        logger.info("Transmission Type Processed")
    except Exception as e:
        raise e 
    
    try: 
        clean_data=fuel_type(clean_data,fuel_type_config_path)
        logger.info("Fuel Type Processed")
    except Exception as e:
        raise e
    
    try:
        clean_data=body_type(clean_data,body_type_config_path)
        logger.info("Body Type Processed")
    except Exception as e:
        raise e
    
    try:
        clean_data=brake_type(clean_data,brake_type_config_path)
        logger.info("Brake Type Processed")
    except Exception as e:
        raise e

    try:
        clean_data=steering_type(clean_data,steering_type_config_path)
        logger.info("Steering Type Processed")
    except Exception as e:
        raise e
    
    try:
        clean_data=drive_type(clean_data,drive_type_config_path)
        logger.info("Drive Type Processed")
    except Exception as e:
        raise e

    try:
        clean_data=gear_type(clean_data,gear_box_config_path)
        logger.info("Gear Type Processed")
    except Exception as e:
        raise e
    
    try:
        clean_data=car_seller_type(clean_data,seller_type_config_path)
        logger.info("Car Seller Type Processed")
    except Exception as e:
        raise e

    try:
        clean_data=owner_type(clean_data,owner_type_config_path)
        logger.info("Owner Type Processed")
    except Exception as e:
        raise e
    
    try:
        clean_data=state(clean_data,state_config_path)
        logger.info("State Processed")
    except Exception as e:
        raise e
    
    try:
        clean_data=model(clean_data,model_config_path)
        logger.info("Model Processed")
    except Exception as e:
        raise e
    

    try:
        clean_data=brand(clean_data,brand_config_path)
        logger.info("Brand Processed")
    except Exception as e:
        raise e
    
    try:
        clean_data=wheel_base(clean_data)
        logger.info("Wheel Base Processed")
    except Exception as e:
        raise e
    
    cols_to_delete=['comfort_features','exterior_features','interior_features',
                    'safety_features','Turning Radius','location','Rear Tread','carType','top_features'
                    ,'Color','Valve_Config','Fuel Suppy System','Cargo_Volume','discountValue','engine_capacity',
                    'Height','Width','Top Speed','Kerb Weight','Max Torque Delivered','Max Torque At',
                    'Engine Type']
    try:
        clean_data.drop(columns=cols_to_delete,axis=1,inplace=True)
        logger.info("Non Essential Columns Deleted")
    except Exception as e:
        raise e
    
    return clean_data

if __name__=='__main__':
    args=ArgumentParser()
    args.add_argument('--config_path','-c',default='params.yaml')
    parsed_args=args.parse_args()
    config_path=parsed_args.config_path
    configs=read_params(config_path)
    final_loc=configs['data_dir']['cars_data_final']
    logger.info("Data Processing Started")

    try:
        clean_data=get_data(configs,pipeline_step='processing')
        clean_data=processing(configs,clean_data)
        logger.info("Data Processing Complete")
        try:
            save_df(clean_data,final_loc)
            logger.info(f"Processed Data Saved at location {final_loc}")
        except Exception as e:
            logger.error(f"Could Not Store Processed Data at location {final_loc}",exc_info=True)
    except Exception as e:
        logger.error("Could Not Finish Data Processing",exc_info=True)

    db.close_connection()
