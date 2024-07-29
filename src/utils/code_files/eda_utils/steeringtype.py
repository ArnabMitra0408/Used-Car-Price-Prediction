import numpy as np
import os
import pandas as pd
import yaml
import zipfile
import shutil

def steeringtype(cars_details_merge):
    cars_details_merge['Steering Type'] = cars_details_merge['Steering Type'].str.replace('electrical', 'power')
    cars_details_merge['Steering Type'] = cars_details_merge['Steering Type'].str.replace('electric', 'power')
    cars_details_merge['Steering Type'] = cars_details_merge['Steering Type'].str.replace('electronic', 'power')
    cars_details_merge['Steering Type'] = cars_details_merge['Steering Type'].str.replace('epas', 'power')
    cars_details_merge['Steering Type'] = cars_details_merge['Steering Type'].str.replace('mt', 'power')
    cars_details_merge['Steering Type'] = cars_details_merge['Steering Type'].str.replace('motor', 'power')
    cars_details_merge['Steering Type'] = cars_details_merge['Steering Type'].str.replace('hydraulic', 'manual')
    cars_details_merge['Steering Type'] = cars_details_merge['Steering Type'].str.replace('hydraulic', 'manual')

    return cars_details_merge
