import pandas as pd
import pickle
from sklearn.preprocessing import OrdinalEncoder

def state(clean_data,state_config_path):
    clean_data=clean_data.reset_index(drop=True)
    state = OrdinalEncoder()
    clean_data['state'] = state.fit_transform(clean_data[['state']])

    with open(state_config_path,'wb') as state_encoder_file:
        pickle.dump(state,state_encoder_file)
    return clean_data