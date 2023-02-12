import pandas as pd
from datetime import datetime
from pandas import DataFrame

def tranform_data_digital(data: DataFrame):
    # TODO
    dataf = data[data['CorreoElectronico'].notnull()]
            
    return dataf