import numpy as np
import pandas as pd

#Drop columns which have more Null rows that null_thresh
def drop_thresh_null(cars_details_merge,null_thresh):
    null_counts = cars_details_merge.isnull().sum()
    columns_to_drop = null_counts[null_counts > null_thresh].index
    cars_details_merge = cars_details_merge.drop(columns=columns_to_drop)
    return cars_details_merge

    