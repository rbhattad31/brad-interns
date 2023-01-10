#import error
"""
try:
    import ayush
except:
    print("No Module found")
"""
#index error
"""
try:
    a=['1','2','3','4']
    print(a[7])
except:
    print("Index out of range")
"""
#keyError
"""
try:
    a={'Name':'Ayush','Age':21,'Role':'RPA'}
    b=input("Enter key")
    if b in a.keys():
        print(b)

except "KeyError" as k:
    print(k)
"""
try:
    a=input("Enter")
    print(a)
except KeyboardInterrupt:
    print("Keyboard Interrupt")
else:
    print("No Exception")