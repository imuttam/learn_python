#Write a Python program that accepts a filename from the user and prints the extension of the file.

file_name = input('Enter filename: ')

try:
    ext = file_name.split('.')
    if len(ext) > 1:
        print(f'Extension of file is: {ext[-1]}')
    else:
        print('Its not a proper file format.')
except:
    print('Its not a proper file format.')

