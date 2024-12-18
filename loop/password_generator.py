import random
import string

alpha = string.ascii_letters
digits = string.digits
special = string.punctuation

password = ''

length = int(input('Enter the length of password:  '))

if length < 6:
    print('Length must be at least of 6 charaters. ')

else:
    for n in range(length-2):
        password += random.choice(alpha)

    password += random.choice(digits)
    password += random.choice(special)

print(password)


