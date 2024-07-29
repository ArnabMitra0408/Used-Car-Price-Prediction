import pandas as pd
import pickle

def drive_type(clean_data,drive_type_config_path):
    clean_data=clean_data.reset_index(drop=True)
    for row in range(clean_data.shape[0]):
        if str(clean_data.loc[row,'Drive Type'])=='nan':
            body_type=clean_data.loc[row,'Body_Type']
            drive_mode=clean_data[clean_data['Body_Type']==body_type]['Drive Type'].mode()
            try:
                clean_data.loc[row,'Drive Type']=drive_mode[0]
            except:
                continue
        else:
            continue
    clean_data['Drive Type'].isna().sum()
    clean_data.dropna(subset=['Drive Type'],inplace=True)

    Drive_Type={'fwd':1,'2wd':2,'rwd':3,'4wd':4,'awd':5,'4x2':6}

    clean_data['Drive Type']=clean_data['Drive Type'].map(Drive_Type)

    with open(drive_type_config_path, 'wb') as Drive_Type_encoding:
        pickle.dump(Drive_Type, Drive_Type_encoding)
    return clean_data
