from openpyxl import load_workbook

wb = load_workbook('ser.xlsx')
ws = wb.get_active_sheet()
for i in ws.values:
    print(i)