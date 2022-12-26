import re

ip = "105.98.094.196"
string = re.sub('\.0*', '.', ip)
print(string)
