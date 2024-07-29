import numpy as np
import pandas as pd

def front_tread(clean_data):
    mean_front_tread={}
    b_types=list(clean_data['Body_Type'].unique())
    clean_data=clean_data.reset_index(drop=True)
    for b_type in b_types:
        b_type_mean=clean_data[clean_data['Body_Type']==b_type]['Front Tread'].mean()
        mean_front_tread[b_type]=b_type_mean

    for row in range(clean_data.shape[0]):
        if str(clean_data.loc[row,'Front Tread'])=='nan':
            clean_data.loc[row,'Front Tread']=mean_front_tread[clean_data.loc[row,'Body_Type']]
    clean_data.dropna(subset=['Front Tread'],inplace=True)
    return clean_data