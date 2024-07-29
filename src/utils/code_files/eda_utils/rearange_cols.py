import numpy as np
import os
import pandas as pd
import yaml
import zipfile
import shutil



def rearange_cols(cars_details_merge,columnlist):
    cars_details_merge = cars_details_merge.reindex(columnlist, axis=1)
    return cars_details_merge