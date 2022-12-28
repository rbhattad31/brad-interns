# os_function file_prosessing operations rename_del
# os.getcwd()-->To get current working directory
import os
cwd = os.getcwd()
print(cwd)
print()
# os.getlogin()--> display who logged in to the system
login = os.getlogin()
print(login)
print()
# os.chdir(path)--> changes the current working directory to given path
# path_of = os.chdir(C:\Users\heman\PycharmProjects\pythonTraining\Day_8)
# print(path_of)

#os.listdir()-->lists all the files in the current directory
list_on = os.listdir()
print(list_on)
print()
#os.makedires() makes dict and requried sub dict's too
#dires = os.makedirs(os.path.join("a", "b","c"))
print(os.path.join("a", "b","c"))
print(dires)