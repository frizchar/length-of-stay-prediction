import pandas as pd


def pull_dataset(hospital: str, number_of_classes: int):
    filename = 'hospital_' + hospital + '_class_' + str(number_of_classes) + '_data.xlsx'
    df =  pd.read_excel(filename)

    return df
