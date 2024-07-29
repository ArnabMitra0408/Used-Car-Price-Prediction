import numpy as np
import os
import pandas as pd
import yaml
import zipfile
import shutil

def drop_duplicate_rows(cars_details_merge):
    cars_details_merge=cars_details_merge.drop_duplicates()
    return cars_details_merge