import csv
with open('people.csv', 'r') as file:  # The csv.reader() is used to read the file,
    # which returns an iterable reader object.The reader object is then iterated using a for loop to print
    # the contents of each row.
    reader = csv.reader(file)
    for row in reader:
        print(row)
