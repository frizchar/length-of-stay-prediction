# perform k-fold cross-validaton on train data

from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import StratifiedKFold
import numpy as np

import split_data


def gridsearch_cv(hospital: int, test_length: int, predictors: list, number_of_classes: int, param_grid: dict):
    # import train data from module 'split_data'
    df_train, df_test, le_map = split_data.split_data(hospital, test_length, predictors, number_of_classes)
    dataset = df_train
    X, y = dataset[predictors], dataset['target']

    if __name__ == "__main__":
        print('scale_pos_weight is :', float(np.sum(y == 0)) / np.sum(y == 1))

    # split into train-test subsets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y)

    if number_of_classes == 2:
        model = XGBClassifier(tree_method='hist', enable_categorical=True,
                              metric='binary', eval_metric='logloss')
    elif number_of_classes == 3:
        model = XGBClassifier(tree_method='hist', enable_categorical=True,
                              metric='multiclass', eval_metric='mlogloss')

    # finalize param_grid
    if number_of_classes == 2:
        param_grid['scale_pos_weight'] = [float(np.sum(y == 0)) / np.sum(y == 1)]
    elif number_of_classes == 3:
        param_grid['num_class'] = [3]

    if __name__ == "__main__":
        print('scale_pos_weight', param_grid['scale_pos_weight'])

    kfold = StratifiedKFold(n_splits=5, shuffle=True, random_state=7)

    # making an object grid_search for GridSearchCV and fitting the dataset i.e X and y
    grid_search = GridSearchCV(model, param_grid, # scoring=gridsearch_cv_metric,
                               n_jobs=4, cv=kfold)

    fit_params = {
        "early_stopping_rounds": 10,
        # "eval_metric": "mae",
        "eval_set": [[X_test, y_test]],
        # "verbose": True,
        }

    grid_result = grid_search.fit(X_train, y_train, **fit_params)

    # print the best set of hyperparameters and the corresponding score
    best_params = grid_result.best_params_
    print("\nBest set of hyperparameters: ", best_params)
    print("Best score: ", grid_search.best_score_)

    return grid_result, best_params, df_test, le_map
