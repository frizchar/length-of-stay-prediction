# split data to train and test subsets

from datetime import timedelta

import encode_data


def split_data(hospital: int, test_length: int, predictors: list, number_of_classes: int):

    hospital = str(hospital)

    # fetch the final dataset
    columns = predictors + ['target', 'datein']
    df, le_map = encode_data.encode_data(hospital, predictors, number_of_classes)
    df = df[columns]
    print('df', df)
    # generate train & test subsets based on split_date
    split_date = str(max(df['datein']).date() - timedelta(days=test_length+1))
    df_train = df.loc[(df['datein'] <= split_date)]
    df_test = df.loc[(df['datein'] > split_date)]

    if __name__ == "__main__":
        print('split date :', split_date, '\n')
        print('max df_train date :', str(max(df_train['datein']).date()), '\n')
        print('min df_test date :', str(min(df_test['datein']).date()), '\n')

    return df_train, df_test, le_map
