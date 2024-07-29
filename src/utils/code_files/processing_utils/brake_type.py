import pandas as pd
import pickle
def brake_type(clean_data,brake_type_config_path):
    clean_data=clean_data.reset_index(drop=True)
    for row in range(clean_data.shape[0]):
        if str(clean_data.loc[row,'Front Brake Type'])=='nan':
            body_type=clean_data.loc[row,'Body_Type']
            brake_mode=clean_data[clean_data['Body_Type']==body_type]['Front Brake Type'].mode()
            clean_data.loc[row,'Front Brake Type']=brake_mode[0]
        elif str(clean_data.loc[row,'Rear Brake Type'])=='nan':
            body_type=clean_data.loc[row,'Body_Type']
            brake_mode=clean_data[clean_data['Body_Type']==body_type]['Rear Brake Type'].mode()
            clean_data.loc[row,'Rear Brake Type']=brake_mode[0]
        else:
            continue

    Brake_Type={'disc':1,'ventilated disc':2,'caliper':3,'drum':4,'disc & drum':5}

    clean_data['Front Brake Type']=clean_data['Front Brake Type'].map(Brake_Type)
    clean_data['Rear Brake Type']=clean_data['Rear Brake Type'].map(Brake_Type)
    clean_data.dropna(subset=['Rear Brake Type'],inplace=True)
    with open(brake_type_config_path, 'wb') as Brake_Type_encoding:
        pickle.dump(Brake_Type, Brake_Type_encoding)
    return clean_data
