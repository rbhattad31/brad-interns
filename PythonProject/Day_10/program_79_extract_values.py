input_string = 'some strings are "present" "in" between "python" "for" "python" '
result = input_string.split()
res=[]

for i in result:
	if i.startswith('"') and i.endswith('"'):
		i=i.replace('"', "")
		res.append(i)
print(res)
