import pandas as pd
import pickle
from sklearn.preprocessing import OrdinalEncoder

def body_type(clean_data,body_type_config_path):
    clean_data=clean_data.reset_index(drop=True)
    clean_data.dropna(subset=['Body_Type'], inplace=True)

    body_type = OrdinalEncoder()
    clean_data['Body_Type'] = body_type.fit_transform(clean_data[['Body_Type']])

    with open(body_type_config_path,'wb') as body_type_encoder_file:
        pickle.dump(body_type,body_type_encoder_file)
    return clean_data