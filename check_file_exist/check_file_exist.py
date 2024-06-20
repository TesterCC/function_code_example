import os

file_path = './a.txt'

if os.path.exists(file_path):
    print("File exist.")
else:
    print("File doesn't exist.")
