# split data to train and test subsets

from datetime import timedelta

import encode_data


def split_data(hospital: int, test_length: int, predictors: list, number_of_classes: int):

    hospital = str(hospital)

    # fetch the final dataset
    columns = predictors + ['target', 'patdatein']
    df, le_map = encode_data.encode_data(hospital, predictors, number_of_classes)
    df = df[columns]
    print('df', df)
    # generate train & test subsets based on split_date
    split_date = str(max(df['patdatein']).date() - timedelta(days=test_length+1))
    df_train = df.loc[(df['patdatein'] <= split_date)]
    df_test = df.loc[(df['patdatein'] > split_date)]

    if __name__ == "__main__":
        print('split date :', split_date, '\n')
        print('max df_train date :', str(max(df_train['patdatein']).date()), '\n')
        print('min df_test date :', str(min(df_test['patdatein']).date()), '\n')

    return df_train, df_test, le_map
