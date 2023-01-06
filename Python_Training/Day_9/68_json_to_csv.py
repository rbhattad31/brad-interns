import json
import csv
import string
print("Program to demostrate conversion of json to csv")
print("\n")
with open('example_2.json') as json_file:
	info = json.loads(json_file)
	print("JSON file JSONdata.json is opened for reading")
print("\n")
emp_info = info['quiz']
csv_file = open('example.csv', 'w')
print("CSV file is opened for writing JSON data")
print("\n")
csv_writer = csv.writer(csv_file)
count = 0
print("Writing headers to file")
print("\n")
for e in emp_info:
	if count == 0:
		header_csv = e.keys()
		csv_writer.writerow(header_csv)
		count += 1
		csv_writer.writerow(e.values())
print("JSON file is converted to CSV file")
csv_file.close()