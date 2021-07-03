import os
from posixpath import split
import pandas as pd
import xlsxwriter

def export_csv(path, folder_name):
    source = path + '/csv/source/' + folder_name
    destination = path + '/xls/destination/' + folder_name + '.xlsx'
    writer = pd.ExcelWriter(destination, engine='xlsxwriter')
    for file in os.listdir(source):  
        reader = pd.read_csv(source + '/' + file, delimiter=';')
        reader.to_excel(writer, sheet_name=file.replace('.csv', ''))
    writer.save()
    writer.close()