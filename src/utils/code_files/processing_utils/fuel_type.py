import pandas as pd
import pickle

def fuel_type(clean_data,fuel_type_config_path):
    clean_data=clean_data.reset_index(drop=True)
    Fuel_Type={'petrol':1,'diesel':2,'cng':3,'lpg':4,'electric':5}

    clean_data['Fuel_Type']=clean_data['Fuel_Type'].map(Fuel_Type)

    with open(fuel_type_config_path, 'wb') as Fuel_Type_encoding:
        pickle.dump(Fuel_Type, Fuel_Type_encoding)
    return clean_data