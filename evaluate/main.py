import pandas as pd

import engine
import output

################################# PARAMETERS

# test run_mode = 'test'
HOSPITAL_list = [1, 2]   # list holding the hospital IDs
test_length = 15  # length of test period
predictors = ['weekday', 'hh24', 'patsex', 'patfamil', 'patter', 'patwayin', 'age',
              'patasfal1', 'has_patasfal2', 'has_patasfal3', 'icdblockid', 'docspec']
number_of_classes = 2
param_grid = {
        'learning_rate': [0.01, 0.015, 0.1, 0.15],
        'max_depth': [5, 6, 7, 8],
        'n_estimators': [40, 50, 60, 70, 80, 90],
        'subsample': [0.9, 0.7],
        'colsample_bytree': [0.9, 0.7],
        'max_delta_step': [1],
    }

#################################

if __name__ == "__main__":
    for hospital in HOSPITAL_list:
        X_test, y_test, y_pred, accuracy_score_, balanced_accuracy_score_, balanced_accuracy_score_adjusted_, \
        recall_score_, le_map, best_params, nbr_test_inpatients, min_test_date, max_test_date, manual_balanced_accuracy_score = \
            engine.run_engine(hospital, test_length, predictors, number_of_classes, param_grid)

        y_test['los_true'] = y_test['los_true'].map(le_map)
        print('nbr ytest :', len(y_test))

        y_pred['los_pred'] = y_pred['los_pred'].map(le_map)
        results = pd.merge(y_test, y_pred, left_index=True, right_index=True)

        output.output_to_excel(hospital, test_length, predictors, results, accuracy_score_,
                               balanced_accuracy_score_, recall_score_, best_params,
                               nbr_test_inpatients, min_test_date, max_test_date, manual_balanced_accuracy_score)
