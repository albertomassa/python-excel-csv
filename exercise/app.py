import sys
import os
from services import excelService
from services import csvService

def export_xls_to_csv(file_name):
    print('method: export_xls_to_csv')
    path = os.path.join(sys.path[0])
    excelService.export_xls(path, file_name)

def export_csv_to_xls(folder_name):
    print('method: export_csv_to_xls')
    path = os.path.join(sys.path[0])
    csvService.export_csv(path, folder_name)

if __name__ == '__main__':
    globals()[sys.argv[1]](sys.argv[2])