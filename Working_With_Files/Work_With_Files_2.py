from os import walk

path = 'C:\Users\zstas\Documents\GitHub\PYTHON_LAB_SZ\Working_With_Files'

files =[]
directories =[]

def file_in_directory_tree(path):
    for (dirpath, dirnames, filenames) in walk(path):
        files.extend(filenames)
        directories.extend(dirnames)
file_in_directory_tree(path)

print (files, directories)
