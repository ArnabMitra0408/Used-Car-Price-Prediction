import numpy as np
import os
import pandas as pd
import yaml
import zipfile
import shutil


def drop_duplicate_col(cars_details_merge):
    columns_to_drop = []
    columns_to_rename = {}

    for col in cars_details_merge.columns:
        if col.endswith('_new'):
            original_col = col[:-4]
            if original_col in cars_details_merge.columns:
                if cars_details_merge[original_col].equals(cars_details_merge[col]):
                    columns_to_drop.append(original_col)
            columns_to_rename[col] = original_col

    cars_details_merge.drop(columns=columns_to_drop,axis=1,inplace=True)

    cars_details_merge.rename(columns=columns_to_rename, inplace=True)
    return cars_details_merge,columns_to_rename