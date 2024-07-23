import os
def list_files(directory):
    files = os.listdir(directory)
    for file in files:
        if os.path.isfile(os.path.join(directory, file)):
            print(file)
directory_path = "D:\Bai tap lam them"
print(directory_path)
list_files(directory_path)