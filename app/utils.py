import openpyxl as opy

import config
def process_bulkupload(filename, fileurl=None):
    file = config.Config.UPLOADED_STUDENTFILES_DEST
    filepath = ''.join([file,'\\',filename])
    # filepath = ''.join(['C:\Users\Sherryl\PycharmProjects\cbaFlask\studentFiles','\\',filename])
    # filepath.replace('\\','/')
    filepath = ''.join([r'C:\Users\Sherryl\PycharmProjects\cbaFlask\studentFiles','/','test2.xlsx'])
    wb = opy.load_workbook(filename=filepath, read_only=True)
    sheet = wb["GA_Template"]

    for row in range(2, sheet.max_row + 1):
        pass
        # process excel here
        # do necessary validations and load it into the db

        # cell_name = "{}{}".format(column, row)
    #     print(([sheet.rows])[0])
        # sheet['A' + str(row)].value
        # sheet['B' + str(row)].value
        # sheet['C' + str(row)].value
        # sheet['D' + str(row)].value
        # sheet['E' + str(row)].value
        # sheet['F' + str(row)].value
        # sheet['G' + str(row)].value
        # sheet['H' + str(row)].value
        # sheet['I' + str(row)].value
        # sheet['J' + str(row)].value
        # sheet['K' + str(row)].value
        # sheet['L' + str(row)].value
        # sheet['M' + str(row)].value
        # sheet['N' + str(row)].value
        # sheet['O' + str(row)].value
        # sheet['P' + str(row)].value
        # sheet['Q' + str(row)].value
        # sheet['R' + str(row)].value
        # sheet['S' + str(row)].value
        # sheet['T' + str(row)].value
        # sheet['U' + str(row)].value
        # sheet['V' + str(row)].value
        # sheet['W' + str(row)].value
        # sheet['X' + str(row)].value
        # sheet['Y' + str(row)].value
        # sheet['Z' + str(row)].value

        # print(sheet['A'+str(row)].value)

process_bulkupload('test2.xlsx')