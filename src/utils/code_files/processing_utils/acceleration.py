import numpy as np
import pandas as pd

def acceleration(clean_data):
    mean_acc={}
    b_types=list(clean_data['Body_Type'].unique())
    clean_data=clean_data.reset_index(drop=True)
    for b_type in b_types:
        b_type_mean=clean_data[clean_data['Body_Type']==b_type]['Acceleration'].mean()
        mean_acc[b_type]=b_type_mean

    for row in range(clean_data.shape[0]):
        if str(clean_data.loc[row,'Acceleration'])=='nan':
            clean_data.loc[row,'Acceleration']=mean_acc[clean_data.loc[row,'Body_Type']]


    clean_data.dropna(subset=['Acceleration'],inplace=True)
    return clean_data