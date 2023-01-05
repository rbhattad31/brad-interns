
import os
"""
cwd = os.getcwd()
print("Current working directory:", cwd)
"""
"""
import os
directory = "Example-1"
parent_dir = "C:/Python-practice/brad-interns/Python_Training"
path = os.path.join(parent_dir, directory)
os.mkdir(path)
print("Directory '% s' created" % directory)
directory = "Example-2"
parent_dir = "C:/Python-practice/brad-interns/Python_Training"
mode = 0o666
path = os.path.join(parent_dir, directory)
os.mkdir(path, mode)
print("Directory '% s' created" % directory)

"""
#listing out files in directory
""" 
import os
path = "C:/Python-practice/brad-interns/Python_Training"
dir_list = os.listdir(path)
print("Files and directories in '", path, "' :")
print(dir_list)
"""

"""
#to delete a file
file = 'file1.txt'
location = "C:/Python-practice/brad-interns/Python_Training"
path = os.path.join(location, file)
os.remove(path)
"""
"""
#to remove a directory
directory = "Example-1"
directory="Example-2"
parent = "C:/Python-practice/brad-interns/Python_Training"
path = os.path.join(parent, directory)
os.rmdir(path)
"""

