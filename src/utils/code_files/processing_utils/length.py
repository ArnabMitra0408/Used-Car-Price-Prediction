import numpy as np
import pandas as pd

def length(clean_data):
    mean_length={}
    b_types=list(clean_data['Body_Type'].unique())
    clean_data=clean_data.reset_index(drop=True)
    for b_type in b_types:
        b_type_mean=clean_data[clean_data['Body_Type']==b_type]['Length'].mean()
        mean_length[b_type]=b_type_mean

    for row in range(clean_data.shape[0]):
        if str(clean_data.loc[row,'Length'])=='nan':
            clean_data.loc[row,'Length']=mean_length[clean_data.loc[row,'Body_Type']]
    clean_data.dropna(subset=['Length'],inplace=True)
    return clean_data