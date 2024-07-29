import pandas as pd
import pickle

def car_seller_type(clean_data,seller_type_config_path):
    Car_Seller_Type={'dealer':1,'individual':2}


    clean_data['Car_Seller_Type']=clean_data['Car_Seller_Type'].map(Car_Seller_Type)

    with open(seller_type_config_path, 'wb') as Car_Seller_Type_encoding:
        pickle.dump(Car_Seller_Type, Car_Seller_Type_encoding)
    return clean_data