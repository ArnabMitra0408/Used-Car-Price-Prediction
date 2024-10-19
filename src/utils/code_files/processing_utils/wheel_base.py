import pandas as pd

def wheel_base(clean_data):
    mean_wheel_base={}
    b_types=list(clean_data['Body_Type'].unique())
    clean_data=clean_data.reset_index(drop=True)
    for b_type in b_types:
        b_type_mean=clean_data[clean_data['Body_Type']==b_type]['Wheel Base'].mean()
        mean_wheel_base[b_type]=b_type_mean

    for row in range(clean_data.shape[0]):
        if str(clean_data.loc[row,'Wheel Base'])=='nan':

            clean_data.loc[row,'Wheel Base']=mean_wheel_base[clean_data.loc[row,'Body_Type']]

    clean_data.dropna(subset=['Wheel Base'],inplace=True)
    return clean_data