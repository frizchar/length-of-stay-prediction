from sklearn.metrics import accuracy_score, balanced_accuracy_score, confusion_matrix, recall_score
import pandas as pd
import sys

import gridsearch_cv


def run_engine(hospital: int, test_length: int, predictors: list, number_of_classes: int,
               param_grid: dict):
    # test correctness of paramater values for hospital and number_of_classes
    if hospital not in [1, 2]:
        sys.exit("wrong 'hospital' value! - program terminated")
    elif number_of_classes not in [2, 3]:
        sys.exit("wrong 'number_of_classes' value! - program terminated")

    # bring test set    
    grid_result, best_params, df_test, le_map = \
        gridsearch_cv.gridsearch_cv(hospital, test_length, predictors, number_of_classes, param_grid)

    nbr_test_inpatients = len(df_test)
    min_test_date = str(min(df_test['patdatein']).date())
    max_test_date = str(max(df_test['patdatein']).date())

    # X_train, y_train = df_train[predictors], df_train['target']
    X_test, y_test = df_test[predictors], df_test['target']
   
    y_pred = grid_result.predict(X_test)

    accuracy_score_ = accuracy_score(y_test, y_pred)
    balanced_accuracy_score_ = balanced_accuracy_score(y_test, y_pred)
    balanced_accuracy_score_adjusted_ = balanced_accuracy_score(y_test, y_pred, adjusted=True)
    if number_of_classes == 2:
        recall_score_ = recall_score(y_test, y_pred)
    elif number_of_classes == 3:
        recall_score_ = recall_score(y_test, y_pred, average='micro')
    confusion_matrix_ = confusion_matrix(y_test, y_pred)

    print('\nMetrics on test set :')
    print('---------------------\n')
    print("accuracy :", accuracy_score_)
    print("balanced_accuracy :", balanced_accuracy_score_)
    print("balanced_accuracy adjusted :", balanced_accuracy_score_adjusted_)
    print("recall :", recall_score_)
    print("confusion_matrix :\n", confusion_matrix_)
    tn, fp, fn, tp = confusion_matrix_.ravel()
    print("TN: ", tn, "\nFP: ", fp, "\nFN: ", fn, "\nTP: ", tp)
    manual_balanced_accuracy_score = 0.5 * ((tp / (tp + fn)) + (tn / (tn + fp)))
    print('manual_balanced_accuracy :', manual_balanced_accuracy_score)

    # convert list 'y_pred' to pandas dataframe
    y_pred = pd.DataFrame(y_pred)
    y_pred.columns = ['los_pred']
    y_pred.index = X_test.index

    y_test = pd.DataFrame(y_test)
    y_test.rename(columns={"target": "los_true"}, inplace=True)

    return X_test, y_test, y_pred, accuracy_score_, balanced_accuracy_score_, \
           balanced_accuracy_score_adjusted_, recall_score_, le_map, best_params, \
           nbr_test_inpatients, min_test_date, max_test_date, manual_balanced_accuracy_score
