import numpy as np
import pandas as pd

def alloy_wheel_size(clean_data):
    clean_data=clean_data[clean_data['Alloy Wheel Size']!=7]
    clean_data=clean_data.reset_index(drop=True)
    for row in range(clean_data.shape[0]):
        if str(clean_data.loc[row,'Alloy Wheel Size'])=='nan':
            tyre_type=clean_data.loc[row,'Tyre Type']
            if str(tyre_type)=='nan':
                continue
            else:
                tyre_mode=clean_data[clean_data['Tyre Type']==tyre_type]['Alloy Wheel Size'].mode()
                try:
                    clean_data.loc[row,'Alloy Wheel Size']=tyre_mode[0]
                except:
                    continue
    clean_data.dropna(subset=['Alloy Wheel Size'],inplace=True)
    return clean_data