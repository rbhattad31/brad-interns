# getting the current working dictionary
import os
cws = os.getcwd()
print("current working dictionary:", cwd)
# changing the current working dictionary
import os


def current_path():
    print("Current working directory before")
    print(os.getcwd())
    print()


current_path()
os.chdir('../')
current_path()

