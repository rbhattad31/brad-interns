import openpyxl
path="C:\Manish B Export Excel files\Agra BP.xlsx"
wb_obj=openpyxl.load_workbook(path)
sheet_obj=wb_obj.active
cell_obj=sheet_obj.cell(row=4,column=2)
print(cell_obj)

