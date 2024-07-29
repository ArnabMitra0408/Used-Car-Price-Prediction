import pandas as pd
import pickle

def steering_type(clean_data,steering_type_config_path):
    clean_data=clean_data.reset_index(drop=True)
    for row in range(clean_data.shape[0]):
        if str(clean_data.loc[row,'Steering Type'])=='nan':
            model_type=clean_data.loc[row,'model']
            steering_mode=clean_data[clean_data['model']==model_type]['Steering Type'].mode()
            try:
                clean_data.loc[row,'Steering Type']=steering_mode[0]
            except:
                continue
        else:
            continue
    clean_data.dropna(subset=['Steering Type'],inplace=True)

    Steering_Type={'power':1,'manual':2}

    clean_data['Steering Type']=clean_data['Steering Type'].map(Steering_Type)


    with open(steering_type_config_path, 'wb') as Steering_Type_encoding:
        pickle.dump(Steering_Type, Steering_Type_encoding)
    return clean_data