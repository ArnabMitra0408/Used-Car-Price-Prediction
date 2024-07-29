import numpy as np
import os
import pandas as pd
import yaml
import zipfile
import shutil

def front_rear_brake(cars_details_merge):
    brake_type_mapping = {}
    brake_type_mapping['disc'] = [
        'disc',
        '260mm discs',
        'disc brakes',
        'disc, 236 mm',
        'discs',
        'disk',
        'multilateral disc',
        'solid disc',
        'electric parking brake',
        'abs',
    ]
    brake_type_mapping['ventilated disc'] = [
        '264mm ventilated discs',
        'booster assisted ventilated disc',
        'caliper ventilated disc',
        'disc brakes with inner cooling',
        'disc,internally ventilated',
        'vantilated disc',
        'ventilated & grooved steel discs',
        'ventilated disc',
        'ventilated disc with twin pot caliper',
        'ventilated discs',
        'ventilated disk',
        'ventillated disc',
        'ventillated discs',
        'ventlated disc',
        'ventilated drum in discs',
        'ventialte disc',
        'ventialted disc',
    ]
    brake_type_mapping['carbon ceramic'] = [
        'carbon ceramic brakes',
        'carbon ceramic brakes.',
    ]
    brake_type_mapping['disc & drum'] = [
        'disc & drum',
        '228.6 mm dia, drums on rear wheels',
        '262mm disc & drum combination',
        'drum in disc',
        'drum in discs',
    ]
    brake_type_mapping['drum'] = [
        'drum',
        '203mm drums',
        'drum`',
        'drums',
        'drums 180 mm',
        'booster assisted drum',
        'drum brakes',
        'leading & trailing drum',
        'leading-trailing drum',
        'self adjusting drum',
        'self adjusting drums',
        'self-adjusting drum',
        'single piston sliding fist',
        'ventilated drum',
        'tandem master cylinder with servo assist',

    ]
    brake_type_mapping['caliper'] = [
        'six piston claipers',
        'twin piston sliding fist caliper',
        'vacuum assisted hydraulic dual circuit w',
        'four piston calipers',
        'disc & caliper type',
    ]

    mapping_dict = {v: k for k, lst in brake_type_mapping.items() for v in lst}
    cars_details_merge['Front Brake Type'] = cars_details_merge['Front Brake Type'].replace(mapping_dict)
    cars_details_merge['Rear Brake Type'] = cars_details_merge['Rear Brake Type'].replace(mapping_dict)

    return cars_details_merge