import pandas as pd
import pickle

def gear_type(clean_data,gear_box_config_path):
    clean_data=clean_data.reset_index(drop=True)
    for row in range(clean_data.shape[0]):
        if str(clean_data.loc[row,'Gear Box'])=='nan':
            body_type=clean_data.loc[row,'Body_Type']
            gear_mode=clean_data[clean_data['Body_Type']==body_type]['Gear Box'].mode()
            try:
                clean_data.loc[row,'Gear Box']=gear_mode[0]
            except:
                continue
        else:
            continue
    Gear_Type={'1 speed':1,'4 speed':2,'5 speed':3,'6 speed':4,'7 speed':5,'8 speed':6
                ,'9 speed':7, '10 speed':8,'direct drive':9,'cvt':10,'fully automatic':11}

    clean_data['Gear Box']=clean_data['Gear Box'].map(Gear_Type)

    with open(gear_box_config_path, 'wb') as Gear_Type_encoding:
        pickle.dump(Gear_Type, Gear_Type_encoding)
    return clean_data