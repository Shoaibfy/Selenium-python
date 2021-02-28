import openpyxl

wk = openpyxl.load_workbook('D:\\Book1.xlsx')

print(wk.sheetnames)  # sheet names
print("Active sheet is :" + str(wk.active))  # Active sheet opened in excel
print(wk.active.title)  # sheet name will be displayed


# creating object of work book sheet

sh = wk['Sheet1']
print(sh.title)
