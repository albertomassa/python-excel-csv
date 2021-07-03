import pandas as pd

def export_xls(path, file_name):
    reader = pd.ExcelFile(path + "/xls/source/" + file_name)
    sheets = reader.sheet_names
    for sheet in sheets: 
        f = pd.read_excel(reader, sheet_name=sheet)
        f.to_csv(path+'/csv/destination/'+sheet+'.csv', index=None, header=True, sep=';')
