import numpy as np
import os
import pandas as pd
import yaml
import zipfile
import shutil

def rename_cols(cars_details_merge,columns_to_rename):
    cars_details_merge.rename(columns=columns_to_rename,inplace=True)
    return cars_details_merge