
from utils.code_files.common_utils import get_begin_float,get_begin_number
import pandas as pd

def get_rpm_average(x):
    x = str(x)
    if '-' in x:
        p1 = get_begin_float(x.split('-')[0])
        p2 = get_begin_float(x.split('-')[1])
        if p1 is None:
            return p2
        if p2 is None:
            return p1
        
        return (p1 + p2)/2
    else:
        return get_begin_float(x)
    
def torque_and_power(cars_details_merge):
    cars_details_merge['Max Power Delivered'] = cars_details_merge['Max Power'].str.split('@').str[0].apply(get_begin_float).astype(float)
    cars_details_merge['Max Power At'] = cars_details_merge['Max Power'].str.split('@').str[1].apply(get_begin_float).astype(float)
    cars_details_merge['Max Torque Delivered'] = cars_details_merge['Max Torque'].str.split('@').str[0].apply(get_begin_float).astype(float)
    cars_details_merge['Max Torque At'] = cars_details_merge['Max Torque'].str.split('@').str[1].apply(get_rpm_average).astype(float)

    cars_details_merge.drop(columns=['Max Power'], inplace=True, axis=1)
    cars_details_merge.drop(columns=['Max Torque'], inplace=True, axis=1)

    return cars_details_merge