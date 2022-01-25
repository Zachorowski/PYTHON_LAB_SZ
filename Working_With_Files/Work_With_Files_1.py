from os import walk

path = 'C:\Users\zstas\Documents\GitHub\PYTHON_LAB_SZ\Working_With_Files'

files =[]
for (dirpath, dirnames, filenames) in walk(path):
    files.extend(filenames)
    break

print (len(files))