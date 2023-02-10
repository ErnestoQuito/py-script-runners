import pandas as pd
from datetime import datetime
from pandas import DataFrame
#import numpy as np

def tranform_data_fisico(data: DataFrame):
    # TODO
    #data = np.where((data['CorreoElectronico'].isnull()) & (data['id']< 1000))
    dataf = data[data['CorreoElectronico'].isnull()]
    
    return dataf

def tranform_data_digital(data: DataFrame):
    # TODO
    dataf = data[data['CorreoElectronico'].notnull()]
        
    return dataf
