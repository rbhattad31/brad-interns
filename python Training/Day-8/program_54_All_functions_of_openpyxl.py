# openpyxl functions
#  Program to print the particular cell value
import openpyxl
path = "C:\\Users\\Admin\\Desktop\\demo.xlsx"
wb_obj = openpyxl. load_workbook(path)
sheet_obj = wb_obj.active
cell_obj = sheet_obj.cell(row=1, column=1)
print(cell_obj.value)
