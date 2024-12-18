import os

file_path= None
files = os.listdir()
for file in files:
    if file.endswith('xlsx'):
        file_path=file
        print(file_path)