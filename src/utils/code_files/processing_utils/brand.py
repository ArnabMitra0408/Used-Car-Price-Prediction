import pandas as pd
import pickle

from sklearn.preprocessing import OrdinalEncoder

def brand(clean_data,brand_config_path):
    clean_data=clean_data.reset_index(drop=True)
    brand = OrdinalEncoder()
    clean_data['brand_name'] = brand.fit_transform(clean_data[['brand_name']])

    with open(brand_config_path,'wb') as brand_encoder_file:
        pickle.dump(brand,brand_encoder_file)
    return clean_data