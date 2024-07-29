import numpy as np
import pandas as pd

def mileage(clean_data):
    mean_mileage={}
    b_types=list(clean_data['Body_Type'].unique())
    clean_data=clean_data.reset_index(drop=True)
    for b_type in b_types:
        b_type_mean=clean_data[clean_data['Body_Type']==b_type]['mileage'].mean()
        mean_mileage[b_type]=b_type_mean

    for row in range(clean_data.shape[0]):
        if str(clean_data.loc[row,'mileage'])=='nan':

            clean_data.loc[row,'mileage']=mean_mileage[clean_data.loc[row,'Body_Type']]

    clean_data.dropna(subset=['mileage'],inplace=True)
    return clean_data