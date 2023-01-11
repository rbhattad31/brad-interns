from zipfile import ZipFile
with ZipFile("C:/Python-practice/brad-interns/Python_Training/demo_zip.zip", 'r') as zObject:
	zObject.extractall(
		path="C:/Python-practice/brad-interns/Python_Training/from zip")
