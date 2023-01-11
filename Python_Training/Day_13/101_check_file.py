import os
if os.path.exists("Demo.txt"):
  print("The file exists")
  size=os.path.getsize('Demo.txt')
  print("The size of the file is" ,size)
else:
  print("The file does not exist")