#Program o find type of character entered by user
import string
special = string.punctuation

char = input('Enter a character: ')

if char.isalpha():
    print('The user has entered a chracter.')

elif char.isdigit():
    print('The user has entered a digit.')

elif char.isspace():
    print('The user has entered a space.')

elif char.isalpha():
    print('The user has entered a chracter.')

elif char in special:
    print('The user has entered a special chracter.')

else:
    print('The user has entered a function key')


