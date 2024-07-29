import numpy as np
import os
import pandas as pd
import yaml
import zipfile
import shutil

def tyretype(cars_details_merge):

    tyre_type_mapping = {}
    tyre_type_mapping['tubeless'] = [
        'tubeless tyres',
        'tubeless',
        'tubeless tyres mud terrain',
        'tubeless tyre',
    ]
    tyre_type_mapping['tubeless radial'] = [
        'tubeless, radial',
        'tubeless,radial',
        'tubeless tyres, radial',
        'tubeless radial tyres',
        'radial, tubeless',
        'radial',
        'tubless, radial',
        'radial tubeless',
        'tubeless radial',
        'tubeless,radials',
        'tubeless radials',
        'radial,tubeless',
        'tubeless radial tyre',
        'radial, tubless',
        'tubless radial tyrees',
        'tubeless , radial',
        'tubeless, radials',
        'radial tyres',
    ]
    tyre_type_mapping['runflat'] = [
        'runflat tyres',
        'runflat',
        'tubeless,runflat',
        'run-flat',
        'runflat tyre',
        'tubeless, runflat',
        'tubeless. runflat',
        'tubeless.runflat',
        'tubeless radial tyrees',
    ]
    tyre_type_mapping['tube'] = [
        'radial with tube',
    ]


    mapping_dict = {v: k for k, lst in tyre_type_mapping.items() for v in lst}
    cars_details_merge['Tyre Type'] = cars_details_merge['Tyre Type'].replace(mapping_dict)

    return cars_details_merge