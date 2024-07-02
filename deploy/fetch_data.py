import pandas as pd
import time
from datetime import datetime


start_time = datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %I:%M:%S %p')


def pull_dataset(hospital: str, number_of_classes: int):
    filename = 'hospital_' + hospital + '_class_' + str(number_of_classes) + '_data.xlsx'
    df =  pd.read_excel(filename)

    return df, start_time
