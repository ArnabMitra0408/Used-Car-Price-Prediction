import numpy as np
import pandas as pd

def num_cylinder(clean_data):
    clean_data=clean_data.reset_index(drop=True)
    for row in range(clean_data.shape[0]):
        if str(clean_data.loc[row,'No of Cylinder'])=='nan':
            if clean_data.loc[row,'Fuel_Type']=='electric':
                clean_data.loc[row,'No of Cylinder']=0.0
            else:
                fuel_type=clean_data.loc[row,'Fuel_Type']
                fuel_mode=clean_data[clean_data['Fuel_Type']==fuel_type]['No of Cylinder'].mode()
                clean_data.loc[row,'No of Cylinder']=fuel_mode[0]
    return clean_data