import pandas as pd
"""
filename = "covid_data.csv"
fields = []
rows = []
with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)
    for row in csvreader:
        rows.append(row)
    print("Total no. of rows: %d" % (csvreader.line_num))

#
print('Field names are:' + ', '.join(field for field in fields))

print('\nFirst 10 rows are:\n')
for row in rows[:10]:
    for col in row:
        print("%10s" % col, end=" "),
    print('\n')
"""
"""
#reading csv files
import csv
with open('covid_data.csv', mode ='r')as file:
    csvFile = csv.reader(file)
    for lines in csvFile:
        print(lines)
"""

csvFile=pd.read_csv("covid_data.csv")
print(csvFile)



