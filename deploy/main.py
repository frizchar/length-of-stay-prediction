import pandas as pd

import engine
import output
import fetch_data

################################# PARAMETERS

# test run_mode = 'prod'
HOSPITAL_list = [1, 2]   # determine the hospital IDs
predictors = ['weekday', 'hh24', 'sex', 'family', 'ter', 'wayin', 'age',
              'asfal1', 'has_asfal2', 'has_asfal3', 'icd10groupid', 'specialty']
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
        X_test, y_test, y_pred, le_map, best_params, start_time = \
            engine.run_engine(hospital, predictors, number_of_classes, param_grid)
        y_pred['los_pred'] = y_pred['los_pred'].map(le_map)

        temp = fetch_data.pull_dataset(str(hospital), number_of_classes)
        columns = ['patdatein']
        y_pred_data = temp[0][columns]
        y_pred_data['hospital'] = str(hospital)
        y_pred_data = y_pred_data.reindex(columns=['hospital', 'datein'])

        results = pd.merge(y_pred_data, y_pred, left_index=True, right_index=True)

        output.output_to_excel(hospital, predictors, results, best_params, start_time)
