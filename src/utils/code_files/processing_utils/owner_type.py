import pandas as pd
import pickle

def owner_type(clean_data,owner_type_config_path):
    clean_data=clean_data.reset_index(drop=True)
    owner_types={'first':1,'second':2,'third':3,'fourth':4,'fifth':5}
    

    clean_data['owner_type']=clean_data['owner_type'].map(owner_types)

    with open(owner_type_config_path, 'wb') as owner_type_encoding:
        pickle.dump(owner_types, owner_type_encoding)
    clean_data.dropna(subset=['owner_type'],inplace=True)
    return clean_data