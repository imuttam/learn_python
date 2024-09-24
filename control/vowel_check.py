# Write a Python program to test whether a passed letter is a vowel or not.

letter = input('Enter a letter pl: ').lower()

vowel = ['a','e','i','o','u']

if letter in vowel:
    print('Entered letter is a Vowel: ')
else:
    print('Entered letter is not a Vowel: ')