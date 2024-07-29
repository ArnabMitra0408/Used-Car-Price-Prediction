import numpy as np
import pandas as pd
import pickle

def tyre_type(clean_data,tyre_types_config_path):
    clean_data=clean_data.reset_index(drop=True)
    tyre_type={'tubeless radial':1,'tubeless':2,'runflat':3,'tube':4}
    clean_data['Tyre Type']=clean_data['Tyre Type'].map(tyre_type)

    with open(tyre_types_config_path, 'wb') as Tyre_Type_encoding:
        pickle.dump(tyre_type, Tyre_Type_encoding)
    clean_data.dropna(subset=['Tyre Type'],inplace=True)
    return clean_data