car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
z = car.clear()  # clear
print(z)

print("_____")

v = car.copy()
print(v)

print("_____")

x = ('key1', 'key2', 'key3')
y = 0
mydict = dict.fromkeys(x, y)  # fromkeys
print(mydict)
print("_____")
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
c = car.get("year")  # get
print(c)
print("_____")

d = car.items()  # items
print(d)
print("_____")

e = car.keys()  # keys
print(e)
print("_____")
f = car.pop("brand")  # pop
print(f)
print("_____")

car.popitem()  # popitem
print(car)
g = car.setdefault("model", "Bronco")  # setdefault
print(g)
print("_____")

car.update({"color": "white"})
print("_____")
h = car.values()
print(h)
print("_____")
