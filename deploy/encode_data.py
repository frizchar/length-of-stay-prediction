# encode loaded data

from sklearn.preprocessing import LabelEncoder
import time

import fetch_data


def encode_data(hospital: int, predictors: list, number_of_classes: int):
    hospital = str(hospital)

    # fetch the final dataset and start_time
    columns = predictors + ['los_group', 'patdatein', 'patdateout_flag']
    tt = fetch_data.pull_dataset(hospital, number_of_classes)
    data = tt[0][columns]
    data = data.rename(columns={'los_group': 'target'})
    start_time = tt[1]

    # start encoding
    encoded_data = data
    # encode predictors
    # encode categorical predictors as "category"
    categorical_predictors = ['patsex', 'patfamil', 'patter', 'patwayin', 'patasfal1',
                              'has_patasfal2', 'has_patasfal3', 'icdblockid', 'docspec']
    encoded_data[categorical_predictors] = encoded_data[categorical_predictors].astype("category")
    # encode numerical predictors as "int64"
    numerical_predictors = ['weekday', 'hh24', 'age']
    encoded_data[numerical_predictors] = encoded_data[numerical_predictors].astype("int64")

    # encode target as labels
    le = LabelEncoder()
    encoded_data['target'] = le.fit_transform(encoded_data['target'])

    # store le as dictionary into variable 'le_mapping'
    le_map = dict(zip(le.transform(le.classes_), le.classes_))

    if __name__ == "__main__":
        print('le mapping :', le_map, '\n')
        print('column data types :\n', encoded_data.dtypes, '\n')

    return encoded_data, le_map, start_time
