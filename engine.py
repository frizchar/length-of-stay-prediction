import pandas as pd
import sys

import gridsearch_cv


def run_engine(hospital: int, predictors: list, number_of_classes: int, param_grid: dict):
    # test correctness of paramater values for hospital and number_of_classes
    if hospital not in [1, 2]:
        sys.exit("wrong 'hospital' value! - program terminated")
    elif number_of_classes not in [2, 3]:
        sys.exit("wrong 'number_of_classes' value! - program terminated")

    # bring test set
    # df_test, le_map, start_time = split_data.split_data(hospital, predictors, number_of_classes)[1:4]
    grid_result, best_params, df_test, le_map, start_time = \
        gridsearch_cv.gridsearch_cv(hospital, predictors, number_of_classes, param_grid)

    # X_train, y_train = df_train[predictors], df_train['target']
    X_test, y_test = df_test[predictors], df_test['target']

    # bring best params
    # grid_result, best_params = gridsearch_cv.gridsearch_cv(hospital, predictors, number_of_classes, param_grid)

    y_pred = grid_result.predict(X_test)

    # convert list 'y_pred' to pandas dataframe
    y_pred = pd.DataFrame(y_pred)
    y_pred.columns = ['los_pred']
    y_pred.index = X_test.index

    y_test = pd.DataFrame(y_test)
    y_test.rename(columns = {"target": "los_true"}, inplace = True)

    return X_test, y_test, y_pred, le_map, best_params, start_time
