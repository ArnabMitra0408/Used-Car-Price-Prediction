import pandas as pd
import pickle

from sklearn.preprocessing import OrdinalEncoder

def model(clean_data,model_config_path):
    clean_data=clean_data.reset_index(drop=True)
    model = OrdinalEncoder()
    clean_data['model'] = model.fit_transform(clean_data[['model']])

    with open(model_config_path,'wb') as model_encoder_file:
        pickle.dump(model,model_encoder_file)
    return clean_data