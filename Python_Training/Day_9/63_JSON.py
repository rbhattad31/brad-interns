import json
x={'Name':'Ayush','Age':21,'Gender':'Male'}
y=json.dumps(x)
print(y)
print(json.dumps("Ayush Bhattad"))
print(json.dumps(24))
print(json.dumps(122.5))
print(json.dumps(True))
print(json.dumps(None))
