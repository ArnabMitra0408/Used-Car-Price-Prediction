
import numpy as np
import os
import pandas as pd
import yaml
import zipfile
import shutil

def drop_unused_col(cars_details_merge):
    cars_details_merge=cars_details_merge.drop(columns=['position','images','imgCount','modelId'
                                    ,'vid','centralVariantId','vlink','pageNo','views'
                                    ,'usedCarId','usedCarSkuId','ucid','sid'
                                    ,'tmGaadiStore','emiwidget','dynx_itemid_x'
                                    ,'dynx_itemid2_x','leadForm','leadFormCta',
                                    'compare','pageType','corporateId','page_title','model_id_new','dealer_id_new','city_id_new',
                                    'page_type','dealer_id','dynx_event','dynx_pagetype','dynx_itemid_y','dynx_itemid2_y',
                                    'dynx_totalvalue_y','template_name_new','page_template','template_Type_new','experiment','dynx_totalvalue_x','pi','threesixty'
                                    ,'city_y','msp','city_x','oem_name','exterior_color','used_carid','variant_name','variant_new','city_name_new','model_name','model_type_new',
                                    'body_type_new','price_range_segment','price_segment','price_segment_new','price',
                                    'car_segment','seller_type_new','transmissionType','seating_capacity_new',
                                    'model_year_new','model_year','transmission_type','km_driven','fuel_type','fuel_type_new','brand_new','vehicle_type_new','transmission_type_new',
                                    'dvn','oem','variantName','offers','car_type_new','min_engine_capacity_new','max_engine_capacity_new','engine_cc'
                                    ],axis=1)
    return cars_details_merge
    
    