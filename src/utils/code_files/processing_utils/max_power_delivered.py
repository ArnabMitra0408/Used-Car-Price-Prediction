import numpy as np
import pandas as pd

def max_power_delivered(clean_data):
    mean_power_delivered={}
    m_types=list(clean_data['model'].unique())
    clean_data=clean_data.reset_index(drop=True)
    for m_type in m_types:
        m_type_mean=clean_data[clean_data['model']==m_type]['Max Power Delivered'].mean()
        mean_power_delivered[m_type]=m_type_mean

    for row in range(clean_data.shape[0]):
        if str(clean_data.loc[row,'Max Power Delivered'])=='nan':
            clean_data.loc[row,'Max Power Delivered']=mean_power_delivered[clean_data.loc[row,'model']]

    clean_data.dropna(subset=['Max Power Delivered'],inplace=True)
    return clean_data