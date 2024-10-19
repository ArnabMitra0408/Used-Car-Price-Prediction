import numpy as np
import pandas as pd

def max_power_at(clean_data):
    mean_power_at={}
    m_types=list(clean_data['model'].unique())
    clean_data=clean_data.reset_index(drop=True)
    for m_type in m_types:
        m_type_mean=clean_data[clean_data['model']==m_type]['Max Power At'].mean()
        mean_power_at[m_type]=m_type_mean

    for row in range(clean_data.shape[0]):
        if str(clean_data.loc[row,'Max Power At'])=='nan':
            clean_data.loc[row,'Max Power At']=mean_power_at[clean_data.loc[row,'model']]

    clean_data.dropna(subset=['Max Power At'],inplace=True)
    return clean_data