from utils.code_files.common_utils import get_begin_float,get_begin_number
import pandas as pd

def numerical_feature(cars_details_merge,feature_to_numerical):
    
    for col in feature_to_numerical:
        cars_details_merge[col] = cars_details_merge[col].apply(get_begin_float).astype(float)

    return cars_details_merge