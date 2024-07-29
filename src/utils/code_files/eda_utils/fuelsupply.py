import numpy as np
import os
import pandas as pd
import yaml
import zipfile
import shutil

def fuelsupply(cars_details_merge):
    fuel_injection_mapping = {
    "Gasoline Port Injection": [
        "intelligent-gas port injection", 
        "i-gpi",
        "dohc",
        "pfi"
    ],
    "Multi-Point Fuel Injection": [
        "mpfi", 
        "multi-point injection", 
        "mpfi+lpg", 
        "mpfi+cng", 
        "multipoint injection", 
        "smpi", 
        "mpi",
        "multi point fuel injection",
        "dpfi",
        "mfi",
        "multi point injection",
        "msds",
        "cng"
    ],
    "Electronic Fuel Injection": [
        "efi(electronic fuel injection)", 
        "efi", 
        "efi (electronic fuel injection)", 
        "efic", 
        "electronic fuel injection", 
        "electronically controlled injection", 
        "electronic injection system", 
        "sefi",
        "egis",
        "efi (electronic fuel injection",
        "efi",
        "efi -electronic fuel injection",
    ],
    "Direct Injection": [
        "direct injection", 
        "direct injectio", 
        "direct fuel injection",
        "direct engine",
    ],
    "Common Rail Injection": [
        "crdi", 
        "common rail", 
        "common rail injection", 
        "common rail direct injection", 
        "common rail direct injection (dci)", 
        "common-rail type", 
        "advanced common rail", 
        "common rail system", 
        "common rail diesel", 
        "pgm-fi (programmed fuel injection)", 
        "pgm-fi (programmed fuel inje", 
        "pgm - fi", 
        "pgm-fi", 
        "pgm-fi (programmed fuel inject",
        "direct injection common rail",
        "cdi"
    ],
    "Distributor-Type Fuel Injection": [
        "dedst", 
        "distribution type fuel injection", 
        "distributor-type diesel fuel injection",
    ],
    "Indirect Injection": [
        "indirect injection",
        "idi"
    ],
    "Gasoline Direct Injection": [
        "gdi", 
        "gasoline direct injection",
        "tfsi",
        "tsi",
        "tgdi"
    ],
    "Turbo Intercooled Diesel": [
        "tcdi", 
        "turbo intercooled diesel",
        "tdci"
    ],
    "Intake Port Injection": [
        "intake port(multi-point)"
    ],
    "Diesel Direct Injection": [
        "ddi", 
        "ddis"
    ],
    "Variable Valve Timing Injection": [
        "dual vvt-i", 
        "vvt-ie", 
        "ti-vct"
    ],
    "Three-Phase AC Induction Motors": [
        "3 phase ac induction motors"
    ],
    "Electric": [
        "electric", 
        "isg"
    ],
    }

    mapping_dict = {v: k for k, lst in fuel_injection_mapping.items() for v in lst}
    cars_details_merge['Fuel Suppy System'] = cars_details_merge['Fuel Suppy System'].replace(mapping_dict)

    return cars_details_merge