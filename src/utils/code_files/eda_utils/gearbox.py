import numpy as np
import os
import pandas as pd
import yaml
import zipfile
import shutil

def gearbox(cars_details_merge):
    gear_box_mapping = {}
    gear_box_mapping['1 speed'] = [
        'single speed', 
        'single speed automatic', 
        'single speed reduction gear', 
        'single-speed transmission',
        'Single-speed transmission',
    'Single Speed','Single Speed Automatic',
    'Single speed reduction gear', 
    ]
    gear_box_mapping['4 speed'] = [
        '4 speed', 
        '4-speed', '4 Speed','4-Speed', '4 Speed '
    ]
    gear_box_mapping['5 speed'] = [
        '5', 
        '5 - speed', 
        '5 gears', 
        '5 manual', 
        '5 speed', 
        '5 speed at+ paddle shifters', 
        '5 speed cvt', 
        '5 speed forward, 1 reverse', 
        '5 speed manual', 
        '5 speed manual transmission', 
        '5 speed+1(r)', 
        '5 speed,5 forward, 1 reverse', 
        '5-speed', 
        '5-speed`', 
        'five speed', 
        'five speed manual', 
        'five speed manual transmission', 
        'five speed manual transmission gearbox',
        '5 Speed',
        '5 Speed ',
        '5-Speed',
        'Five Speed Manual Transmission',
        '5 Speed+1(R)',
        '5 Speed Forward, 1 Reverse',
        '5 Speed,5 Forward, 1 Reverse',
        '5-Speed ',
        '5 Speed Manual',
        '5 Gears ',
        '5 Speed Manual Transmission',
        '5 Speed+1(R)',
        '5 speed',
        'Five Speed Manual Transmission Gearbox',
    'Five Speed',
    'Five Speed Manual',
    '5 Speed CVT','5 Speed AT+ Paddle Shifters','5-Speed`',
    '5 Manual','5 - Speed', 
    ]
    gear_box_mapping['6 speed'] = [
        '6', 
        '6 speed', 
        '6 speed at', 
        '6 speed automatic', 
        '6 speed geartronic', 
        '6 speed imt', 
        '6 speed ivt', 
        '6 speed mt', 
        '6 speed with sequential shift', 
        '6-speed', 
        '6-speed at', 
        '6-speed automatic', 
        '6-speed autoshift', 
        '6-speed cvt', 
        '6-speed dct', 
        '6-speed imt', 
        '6-speed ivt', 
        '6-speed`', 
        'six speed  gearbox', 
        'six speed automatic gearbox', 
        'six speed automatic transmission', 
        'six speed geartronic, six speed automati', 
        'six speed manual', 
        'six speed manual transmission', 
        'six speed manual with paddle shifter',
        '6 Speed','6-Speed','6-Speed iMT','Six Speed  Gearbox','6 Speed Automatic',
        '6 Speed with Sequential Shift','6 Speed ','6 Speed iMT','6 Speed MT','Six Speed Manual Transmission',
    'Six Speed Automatic Transmission',
    '6 speed','Six Speed Manual', '6-Speed IVT',
    '6-Speed AT', '6-speed CVT',
    '6-Speed DCT','6-speed DCT','6-Speed Automatic','6 Speed Geartronic','6 Speed AT','6-Speed`','6-speed AutoSHIFT',
    '6-Speed IMT',
    
    '6 speed ',
    '6 Speed IMT',
    '6 Speed IVT',
    '6-speed IVT','Six Speed Manual with Paddle Shifter','Six Speed Automatic Gearbox',
    
    'Six Speed Geartronic, Six Speed Automati', 
    ]
    gear_box_mapping['7 speed'] = [
        '7 speed', 
        '7 speed 7g-dct', 
        '7 speed 9g-tronic automatic', 
        '7 speed cvt', 
        '7 speed dct', 
        '7 speed dsg', 
        '7 speed dual clutch transmission', 
        '7 speed s tronic', 
        '7-speed', 
        '7-speed dct', 
        '7-speed dsg', 
        '7-speed pdk', 
        '7-speed s tronic', 
        '7-speed s-tronic', 
        '7-speed steptronic', 
        '7-speed stronic', 
        '7g dct 7-speed dual clutch transmission', 
        '7g-dct', 
        '7g-tronic automatic transmission',
        'amg 7-speed dct',	
        'mercedes benz 7 speed automatic',
        '7 Speed 9G-Tronic automatic',
        '7-Speed DCT',
        '7 Speed',
        '7 Speed CVT',
        '7-Speed','7 Speed DSG',
    '7-Speed DSG', '7 speed',
    '7-speed DSG', '7 Speed 7G-DCT',
    '7G DCT 7-Speed Dual Clutch Transmission ','7G-DCT','7G-TRONIC Automatic Transmission',
    'AMG 7-SPEED DCT','7-Speed Steptronic','7 Speed DCT',

    '7-Speed S-Tronic ', '7-Speed S-Tronic',
    '7-Speed S tronic',
    '7-speed Stronic',
    '7 Speed S tronic',
    '7 Speed ',
    '7 Speed S Tronic','7-speed PDK',
    '7 Speed dual clutch transmission',
    
    
    '7-speed DCT','Mercedes Benz 7 Speed Automatic'
    ]
    gear_box_mapping['8 speed'] = [
        '8', 
        '8 speed', 
        '8 speed cvt', 
        '8 speed multitronic', 
        '8 speed sport', 
        '8 speed tip tronic s', 
        '8 speed tiptronic', 
        '8-speed', 
        '8-speed automatic', 
        '8-speed automatic transmission', 
        '8-speed dct', 
        '8-speed steptronic', 
        '8-speed steptronic sport automatic transmission', 
        '8-speed tiptronic', 
        '8speed',
        'amg speedshift dct 8g',  '8-Speed', '8 speed',
    '8 Speed',
    '8 Speed Sport','8-Speed DCT', '8-Speed Steptronic',
    '8-Speed ', '8-Speed Steptronic Sport Automatic Transmission',
    '8-Speed Automatic Transmission','AMG SPEEDSHIFT DCT 8G',
    '8 Speed ', '8 Speed Tiptronic',
    '8 Speed Multitronic',
    '8 Speed CVT', '8Speed',
    '8 Speed Tip Tronic S',
    ]
    gear_box_mapping['9 speed'] = [
        '9 -speed', 
        '9 speed', 
        '9 speed tronic', 
        '9-speed', 
        '9-speed automatic', 
        '9g tronic', 
        '9g-tronic', 
        '9g-tronic automatic', 
        'amg speedshift 9g tct automatic',
        '9 Speed',
    'AMG Speedshift 9G TCT Automatic',
    

    '9G-TRONIC','9 speed Tronic',
    
    
    '9G TRONIC',
    '9G-TRONIC automatic',
    '9 speed', '9-Speed'
    ]
    gear_box_mapping['10 speed'] = [
        '10 speed', '10 Speed',
    '10 speed',
    ]
    gear_box_mapping['cvt'] = [
    'cvt', 
    'e-cvt', 
    'ecvt','E-CVT',
    
    'CVT',
    'eCVT' 
    ]
    gear_box_mapping['direct drive'] = [
    'direct drive', 'Direct Drive'
    ]
    gear_box_mapping['fully automatic'] = [
        'automatic transmission', 
        'fully automatic','Fully Automatic','Automatic Transmission'
    ]
    gear_box_mapping[np.nan] = [
    'nan',
    'ags', 
    'imt', 
    'ivt','IVT','AGS',
    'iMT'
    ]

    mapping_dict = {v: k for k, lst in gear_box_mapping.items() for v in lst}
    cars_details_merge['Gear Box'] = cars_details_merge['Gear Box'].replace(mapping_dict)

    return cars_details_merge