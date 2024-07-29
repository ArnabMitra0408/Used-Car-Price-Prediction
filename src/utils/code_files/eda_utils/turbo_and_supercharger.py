import pandas as pd
def turbo_and_supercharger(cars_details_merge):
    cars_details_merge['Turbo Charger'] = cars_details_merge['Turbo Charger'].replace('yes', True)
    cars_details_merge['Turbo Charger'] = cars_details_merge['Turbo Charger'].replace('no', False).astype(bool)

    cars_details_merge['Super Charger'] = cars_details_merge['Turbo Charger'].replace('yes', True)
    cars_details_merge['Super Charger'] = cars_details_merge['Turbo Charger'].replace('no', False).astype(bool)
    return cars_details_merge
