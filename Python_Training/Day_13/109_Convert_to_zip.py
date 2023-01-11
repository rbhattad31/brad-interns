import shutil
import os.path
archived = shutil.make_archive('C:/Python-practice/brad-interns/Python_Training/demo_zip', 'zip','C:/Python-practice/brad-interns/Python_Training/demo' )

if os.path.exists('C:/Python-practice/brad-interns/Python_Training/demo'):
   print(archived)
else:
   print("ZIP file not created")