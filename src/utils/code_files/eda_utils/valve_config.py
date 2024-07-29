import numpy as np
import os
import pandas as pd
import yaml
import zipfile
import shutil

def valve_config(cars_details_merge):
    cars_details_merge['Valve_Config'] = cars_details_merge['Valve_Config'].str.replace('DOHC with VIS', 'DOHC')
    cars_details_merge['Valve_Config'] = cars_details_merge['Valve_Config'].str.replace('DOHC with VGT', 'DOHC')
    cars_details_merge['Valve_Config'] = cars_details_merge['Valve_Config'].str.replace('16-valve DOHC layout', 'DOHC')
    cars_details_merge['Valve_Config'] = cars_details_merge['Valve_Config'].str.replace('DOHC with TIS', 'DOHC')
    cars_details_merge['Valve_Config'] = cars_details_merge['Valve_Config'].str.replace('DOHC ', 'DOHC')

    # Replace `undefined`, `mpfi`, `vtec` with `NaN`
    cars_details_merge['Valve_Config'] = cars_details_merge['Valve_Config'].str.replace('undefined', 'nan')
    cars_details_merge['Valve_Config'] = cars_details_merge['Valve_Config'].str.replace('MPFi', 'nan')
    cars_details_merge['Valve_Config'] = cars_details_merge['Valve_Config'].str.replace('VTEC', 'nan')
    return cars_details_merge
