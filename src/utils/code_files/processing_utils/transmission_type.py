import pandas as pd
import pickle

def transmission_type(clean_data,transmission_type_config_path):
    clean_data=clean_data.reset_index(drop=True)
    Transmission_Type={'manual':1,'automatic':2}

    clean_data['Transmission_Type']=clean_data['Transmission_Type'].map(Transmission_Type)

    with open(transmission_type_config_path, 'wb') as Transmission_Type_encoding:
        pickle.dump(Transmission_Type, Transmission_Type_encoding)
    return clean_data