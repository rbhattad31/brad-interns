import os

cwd = os.getcwd()
print("Current working directory:", cwd)
path = "/"
dir_list = os.listdir(path)

print("Files and directories in ", path, " : ")
print(dir_list)
