import os
"""
directory = "Demo"
parent_dir = "C:/Python-practice/brad-interns/Python_Training/"
path = os.path.join(parent_dir, directory)
os.mkdir(path)
print("Directory '% s' created" % directory)
"""
"""
path = 'C:/Python-practice/brad-interns/Python_Training/Demo/'
file = 'Demo1.txt'
with open(os.path.join(path, file), 'w') as fp:
    pass
"""
"""
import time
path = "C:/Python-practice/brad-interns/Python_Training/Demo/Demo1.txt"
ti_c = os.path.getctime(path)
ti_m = os.path.getmtime(path)
c_ti = time.ctime(ti_c)
m_ti = time.ctime(ti_m)

print(f"The file located at the path {path} \
was created at {c_ti} and was "
	f"last modified at {m_ti}")
"""
"""
path="C:/Python-practice/brad-interns/Python_Training/"
dir_list=os.listdir(path)
print(dir_list)
"""
"""
os.remove("C:/Python-practice/brad-interns/Python_Training/Demo/Demo1.txt")
"""
os.rmdir("C:/Python-practice/brad-interns/Python_Training/Demo/")




