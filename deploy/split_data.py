# split data to train and todays' subsets

import pandas as pd

import encode_data


def split_data(hospital: int, predictors: list, number_of_classes: int):

    hospital = str(hospital)

    # fetch the final dataset
    columns = predictors + ['target', 'patdatein', 'patdateout_flag']
    df, le_map, start_time = encode_data.encode_data(hospital, predictors, number_of_classes)
    df = df[columns]
    print('df', df)

    # generate train & test subsets
    split_date = pd.to_datetime('today').normalize()
    df_train = df[(df['patdateout_flag'] == 'non_null_patdateout')]
    df_test = df[(df['patdateout_flag'] == 'null_patdateout')]
    df_test = df_test[(df_test['patdatein'] >= split_date)]  # estimate the los only of today's inpatients

    if __name__ == "__main__":
        print('split date :', split_date, '\n')
        print('max df_train date :', str(max(df_train['patdatein']).date()), '\n')

    return df_train, df_test, le_map, start_time
