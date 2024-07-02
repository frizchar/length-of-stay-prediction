# save best_params and test results to excel

import pandas as pd
import json


def output_to_excel(hospital: int, predictors: list, results: pd.DataFrame, best_params: dict, start_time):

    def generate_short_hospital_name(hospital):
        if hospital == 1:
            return 'hospital_1'
        elif hospital == 2:
            return 'hospital_2'
        else:
            return "-"

    folder_path = './data_pool/'
    filename = "los_prod_" + generate_short_hospital_name(hospital) + '.xlsx'
    file_path = folder_path + filename
    writer = pd.ExcelWriter(path=file_path, engine='xlsxwriter')
    workbook = writer.book

    # Start from cell A1
    sheetname = 'los_forecast_' + generate_short_hospital_name(hospital)
    results.to_excel(writer, sheet_name=sheetname, index=True, startrow=0, startcol=0)
    cell_format_2 = workbook.add_format({'bold': True, 'font_color': 'black'})
    worksheet = writer.sheets[sheetname]
    worksheet.autofit()

    sheetname1 = 'los_prod_meta_' + generate_short_hospital_name(hospital)
    worksheet1 = workbook.add_worksheet(sheetname1)

    worksheet1.write('A1', 'Hospital', cell_format_2)
    worksheet1.write('A2', hospital)
    worksheet1.write('B1', 'start_time', cell_format_2)
    worksheet1.write('B2', start_time)
    worksheet1.write('C1', 'test length', cell_format_2)
    worksheet1.write('C2', 'RUN_MODE = PROD')
    worksheet1.write('D1', 'predictors', cell_format_2)
    worksheet1.write('D2', str(predictors))
    worksheet1.write('E1', 'test best params', cell_format_2)
    worksheet1.write('E2', json.dumps(best_params))

    worksheet1.autofit()

    writer.close()

    return
