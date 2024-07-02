# save best_params and test results to excel

import pandas as pd
import json


def output_to_excel(hospital: int, test_length: int, predictors: list, results: pd.DataFrame,
                    accuracy_score_: float, balanced_accuracy_score_: float, recall_score_: float, best_params: dict,
                    nbr_test_inpatients: int, min_test_date, max_test_date, manual_balanced_accuracy_score):

    def generate_short_hospital_name(hospital):
        if hospital == 1:
            return 'hospital_1'
        elif hospital == 2:
            return 'hospital_2'
        else:
            return "-"

    folder_path = './data_pool/'
    filename = "los_test_" + generate_short_hospital_name(hospital) + '.xlsx'
    file_path = folder_path + filename
    writer = pd.ExcelWriter(path=file_path, engine='xlsxwriter')
    workbook = writer.book

    # Start from cell A1
    results.to_excel(writer, sheet_name='predictions_on_test_set', index=True, startrow=0, startcol=0)
    cell_format_2 = workbook.add_format({'bold': True, 'font_color': 'black'})
    worksheet = writer.sheets['predictions_on_test_set']
    worksheet.autofit()

    sheetname1 = 'los_test_meta_' + generate_short_hospital_name(hospital)
    worksheet1 = workbook.add_worksheet(sheetname1)

    worksheet1.write('A1', 'hospital', cell_format_2)
    worksheet1.write('A2', hospital)
    worksheet1.write('B1', 'test_length', cell_format_2)
    worksheet1.write('B2', test_length)
    worksheet1.write('C1', 'nbr_test_inpatients', cell_format_2)
    worksheet1.write('C2', nbr_test_inpatients)
    worksheet1.write('D1', 'min_test_date', cell_format_2)
    worksheet1.write('D2', min_test_date)
    worksheet1.write('E1', 'max_test_date', cell_format_2)
    worksheet1.write('E2', max_test_date)
    worksheet1.write('F1', 'predictors', cell_format_2)
    worksheet1.write('F2', str(predictors))
    worksheet1.write('G1', 'test best params', cell_format_2)
    worksheet1.write('G2', json.dumps(best_params))
    worksheet1.write('H1', 'accuracy_score', cell_format_2)
    worksheet1.write('H2', accuracy_score_)
    worksheet1.write('I1', 'balanced_accuracy_score', cell_format_2)
    worksheet1.write('I2', balanced_accuracy_score_)
    worksheet1.write('J1', 'manual_balanced_accuracy_score', cell_format_2)
    worksheet1.write('J2', manual_balanced_accuracy_score)
    worksheet1.write('K1', 'recall_score', cell_format_2)
    worksheet1.write('K2', recall_score_)

    worksheet1.autofit()

    writer.close()

    return
