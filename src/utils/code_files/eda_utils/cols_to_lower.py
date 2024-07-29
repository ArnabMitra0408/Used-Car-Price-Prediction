import numpy as np
import os
import pandas as pd
import yaml
import zipfile
import shutil

def cols_to_lower(cars_details_merge,cols):
    for col in cols:
        cars_details_merge[col] = cars_details_merge[col].astype(str).str.strip().str.lower()
    return cars_details_merge