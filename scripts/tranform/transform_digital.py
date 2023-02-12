import pandas as pd
from datetime import datetime
from pandas import DataFrame

def tranform_data_digital(data: DataFrame):
    # TODO
    dataf = data[data['correo_electronico'].notnull()]
            
    return dataf