import pandas as pd
df = pd.read_csv("sample text.txt")
print(df.head(10))
print(df.drop_duplicates())
print(df.drop_duplicates(subject=['company']))
print(df.drop_duplicate(subject=['fuel-type', 'body-style']))
print(df.drop_duplicate(subject=['fuel-type', 'body-style'], keep='last'))
# for duplicate removal
# (.*)\n\1\n
# $1\n

# outputfile = open('C:\Users\venkata durga prasad\python Training')
# inputfile = open('C:\Users\venkata durga prasad\python Training')
# lines_seen_so_far = set()
# for line in inputfile:
#    if line not in lines_seen_so_far:
#        outputfile.write(line)
#        lines_seen_so_far.add(line)
# inputfile.close()
# outputfile.close()


#
