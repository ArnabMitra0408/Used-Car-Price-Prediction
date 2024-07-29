import numpy as np
import os
import pandas as pd
import yaml
import zipfile
import shutil

def turbocharger(cars_details_merge):
    cars_details_merge['Turbo Charger'] = cars_details_merge['Turbo Charger'].str.replace('NO', 'No')
    cars_details_merge['Turbo Charger'] = cars_details_merge['Turbo Charger'].str.replace('no', 'No')
    cars_details_merge['Turbo Charger'] = cars_details_merge['Turbo Charger'].str.replace('yes', 'Yes')
    cars_details_merge['Turbo Charger'] = cars_details_merge['Turbo Charger'].str.replace('twin', 'Yes')
    cars_details_merge['Turbo Charger'] = cars_details_merge['Turbo Charger'].str.replace('Turbo', 'Yes')
    cars_details_merge['Turbo Charger'] = cars_details_merge['Turbo Charger'].str.replace('Twin', 'Yes')
    cars_details_merge['Turbo Charger'] = cars_details_merge['Turbo Charger'].str.replace('YES', 'Yes')
    return cars_details_merge
