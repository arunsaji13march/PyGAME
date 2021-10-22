import openpyxl
wb=openpyxl.load_workbook('firstexe.xlsx')
print(wb.sheetnames())