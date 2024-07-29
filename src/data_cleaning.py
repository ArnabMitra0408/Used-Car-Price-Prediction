#Importing Libraries
import pandas as pd
from argparse import ArgumentParser
import logging
from utils.code_files import common_utils
from utils.code_files.common_utils import read_params,save_df,get_begin_float,get_begin_number
from utils.code_files.eda_utils.drop_thresh_null import drop_thresh_null
from utils.code_files.eda_utils.drop_unused_col import drop_unused_col
from utils.code_files.eda_utils.drop_duplicate_cols import drop_duplicate_col
from utils.code_files.eda_utils.rename_cols import rename_cols
from utils.code_files.eda_utils.rearange_cols import rearange_cols
from utils.code_files.eda_utils.drop_duplicate_rows import drop_duplicate_rows
from utils.code_files.eda_utils.cols_to_lower import cols_to_lower
from utils.code_files.eda_utils.valve_config import valve_config
from utils.code_files.eda_utils.gearbox import gearbox
from utils.code_files.eda_utils.drivetype import drivetype
from utils.code_files.eda_utils.steeringtype import steeringtype
from utils.code_files.eda_utils.front_rear_brake import front_rear_brake
from utils.code_files.eda_utils.tyretype import tyretype
from utils.code_files.eda_utils.fuelsupply import fuelsupply
from utils.code_files.eda_utils.numerical_feature import numerical_feature
from utils.code_files.eda_utils.torque_and_power import torque_and_power
from utils.code_files.eda_utils.turbo_and_supercharger import turbo_and_supercharger
from utils.code_files.eda_utils.turbocharger import turbocharger
logger = logging.getLogger(__name__)

def clean_data(configs):

   raw_data_loc=configs['data_dir']['cars_details_merge']
   clean_data_loc=configs['data_dir']['cars_data_clean']
   null_thresh=configs['data_cleaning']['null_thresh']
   cars_details_merge=pd.read_csv(raw_data_loc)

   #All the functions to clean the data
   try:
      cars_details_merge=drop_thresh_null(cars_details_merge,null_thresh)
      logging.info(f"Successfully Dropped Columns which have more than {null_thresh} Null values")
   except Exception as e:
      raise e

   try:
      cars_details_merge=drop_unused_col(cars_details_merge)
      logging.info("Successfully Dropped Unused Columns")
   except Exception as e:
        raise e
    
   try: 
      cars_details_merge,columns_to_rename=drop_duplicate_col(cars_details_merge)
      logging.info("Successfully Deleted Duplicated Columns and Stored the Columns to Rename")
   except Exception as e:
      raise e

   try:
      combined_columns_to_rename=columns_to_rename.copy()
      combined_columns_to_rename.update({"loc": "location", "myear": "Manufactured_Year",
                                    "bt":"Body_Type",'tt':'Transmission_Type',
                                    "ft":"Fuel_Type","ip":"Insurance_Premium",
                                    "No Door Numbers":"Num_Doors","pu":"Listed_Price",'Value Configuration':"Valve_Config",
                                    "Values per Cylinder":"Valves_Per_Cylinder", 'utype':'Car_Seller_Type','Cargo Volumn':'Cargo_Volume','km':'KM_Driven'
                                    })

      cars_details_merge=rename_cols(cars_details_merge,combined_columns_to_rename)
      logging.info("Succesfully Renamed Columns")
   except Exception as e:
      raise e


   cols_to_rearrange=['brand_name','model', 'location','state','Manufactured_Year','owner_type','Body_Type', 'Transmission_Type','Insurance_Premium','Fuel_Type', 'KM_Driven','discountValue',
       'Car_Seller_Type', 'carType', 'top_features', 'comfort_features',
       'interior_features', 'exterior_features', 'safety_features', 'Color',
       'Engine Type', 'Displacement', 'Max Power', 'Max Torque',
       'No of Cylinder', 'Valves_Per_Cylinder', 'Valve_Config',
       'Turbo Charger', 'Super Charger', 'Length', 'Width', 'Height',
       'Wheel Base', 'Front Tread', 'Rear Tread', 'Kerb Weight', 'Gear Box',
       'Drive Type', 'Seating Capacity', 'Steering Type', 'Turning Radius',
       'Front Brake Type', 'Rear Brake Type', 'Top Speed', 'Acceleration',
       'Tyre Type', 'Num_Doors', 'Cargo_Volume',
       'engine_capacity', 'mileage',
       'Fuel Suppy System', 'Alloy Wheel Size','Listed_Price']
   try:
      cars_details_merge=rearange_cols(cars_details_merge,cols_to_rearrange)
      logging.info("Successfully Rearranged Columns")
   except Exception as e:
      raise e

   try:
      cars_details_merge=drop_duplicate_rows(cars_details_merge)
      logging.info("Successfully Dropped Duplicate Rows")
   except Exception as e:
      raise e
    #Cols to Lower
   columns_str_to_lower = [
    'location', 'state', 'Manufactured_Year',
       'owner_type', 'Body_Type', 'Transmission_Type', 'Insurance_Premium',
       'Fuel_Type', 'Car_Seller_Type', 'carType',
       'top_features', 'comfort_features', 'interior_features',
       'exterior_features', 'safety_features', 'Color', 'Engine Type',
       'Displacement', 'Max Power', 'Max Torque', 'No of Cylinder',
       'Valves_Per_Cylinder', 'Valve_Config', 'Turbo Charger', 'Super Charger',
       'Length', 'Width', 'Height', 'Wheel Base', 'Front Tread', 'Rear Tread',
       'Kerb Weight', 'Gear Box', 'Drive Type', 'Seating Capacity',
       'Steering Type', 'Turning Radius', 'Front Brake Type',
       'Rear Brake Type', 'Top Speed', 'Acceleration', 'Tyre Type', 'Cargo_Volume', 'mileage',
       'Fuel Suppy System', 'Alloy Wheel Size'
    ]

   try:
      cars_details_merge=cols_to_lower(cars_details_merge,columns_str_to_lower)
      logging.info("Successfully Converted the Column Entries to lower case")
   except Exception as e:
      raise e    
   
   try:
      cars_details_merge=valve_config(cars_details_merge)
      logging.info("Successfully Cleaned Valve Config Column")
   except Exception as e:
      raise e

   try:
      cars_details_merge=turbocharger(cars_details_merge)
      logging.info("Successfully Cleaned TurboCharger Column")
   except Exception as e:
      raise e

   try:
      cars_details_merge=gearbox(cars_details_merge)
      logging.info("Successfully Cleaned Gear Box Column")
   except Exception as e:
      raise e

   try:
      cars_details_merge=drivetype(cars_details_merge)
      logging.info("Successfully Cleaned Drive Type Column")
   except Exception as e:
      raise e

   try: 
      cars_details_merge=steeringtype(cars_details_merge)
      logging.info("Successfully Cleaned Steering Type Column")
   except Exception as e:
      raise e

   try:
      cars_details_merge=front_rear_brake(cars_details_merge)
      logging.info("Successfully Cleaned Front and Rear Brake Columns")
   except Exception as e:
      raise e

   try:
      cars_details_merge=tyretype(cars_details_merge)
      logging.info("Successfully Cleaned Tyre Type Column")
   except Exception as e:
      raise e

   try:
      cars_details_merge=fuelsupply(cars_details_merge)
      logging.info("Successfully Cleaned, Fuel Supply Column")
   except Exception as e:
      raise e
   
   try:
      cars_details_merge=torque_and_power(cars_details_merge)
      logging.info("Successfully Cleaned Torque and Power Columns")
   except Exception as e:
      raise e


   try:
      cars_details_merge=turbo_and_supercharger(cars_details_merge)
      logging.info("Successfully Converted TurboCharger and SuperCharger Columns to Boolena")
   except Exception as e:
      raise e

   feature_to_numerical=['Listed_Price','Length', 'Width', 'Height', 
                      'Wheel Base','Front Tread', 'Rear Tread','Kerb Weight'
                      ,'Turning Radius','Top Speed','Acceleration'
                      ,'Alloy Wheel Size','KM_Driven','Cargo_Volume','mileage']
   try:
      cars_details_merge=numerical_feature(cars_details_merge,feature_to_numerical)
      logging.info("Successfully Got The Numerical Data From the Features")
   except Exception as e:
      raise e
   return cars_details_merge,clean_data_loc
    

if __name__=="__main__":
   args=ArgumentParser()
   args.add_argument("--config_path", '-c', default='params.yaml')
   parsed_args=args.parse_args()
   configs=read_params(parsed_args.config_path)
   
   logging.info(f"Data Cleaning Started")
   try:
      clean_data,clean_data_loc=clean_data(configs)
      logging.info("Data Cleaning Successful")
      try:
         save_df(clean_data,clean_data_loc)
         logging.info(f"Cleaned Data Saved in location {clean_data_loc}")
      except Exception as e:
         logging.error(f"Cleaned Data Could Not Be Saved in location {clean_data_loc}",exc_info=True)
   except Exception as e:
      logging.error(f"Data Cleaning Failed",exc_info=True)

   