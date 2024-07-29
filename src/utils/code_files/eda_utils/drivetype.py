import numpy as np
import os
import pandas as pd
import yaml
import zipfile
import shutil

def drivetype(cars_details_merge):
    drive_type_mapping = {}
    drive_type_mapping['fwd'] = ['fwd', 'front wheel drive']
    drive_type_mapping['2wd'] = ['2wd', 'two wheel drive', '2 wd', 'two whhel drive']
    drive_type_mapping['rwd'] = ['rwd', 'rear wheel drive with esp', 'rear-wheel drive with esp', 'rwd(with mtt)']
    drive_type_mapping['awd'] = ['awd', 'all wheel drive', 'all-wheel drive with electronic traction', 'permanent all-wheel drive quattro']
    drive_type_mapping['4wd'] = ['4wd', '4 wd', '4x4', 'four whell drive']
    drive_type_mapping['nan'] = ['nan', '3']

    mapping_dict = {v: k for k, lst in drive_type_mapping.items() for v in lst}
    cars_details_merge['Drive Type'] = cars_details_merge['Drive Type'].replace(mapping_dict)

    return cars_details_merge
