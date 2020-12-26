def read_excel_sheets(xls_path):
    #read all sheets of an excel workbook

    print(f'Loading {xls_path} into pandas')
    xl = pd.ExcelFile(xls_path)
    df = pd.DataFrame()
    columns = None
    for idx, name in enumerate(xl.sheet_names):
        print(f'Reading sheet #{idx} : {name}')
        sheet = xl.parse(name)
        if idx == 0:
            # read the columns of the sheet
            columns = sheet.columns
        sheet.columns = columns
        # Add sheet name as column
        sheet['sheet'] = name.split(' ')[-1]
        df = df.append(sheet, ignore_index=True)
    return df
