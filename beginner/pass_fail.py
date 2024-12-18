# Write a program to read marks of 10 students and decide weather student is pass or fail.

passed = 0
failed = 0
counter = 0
while counter < 10:
    marks = int(input('Enter the marks: '))
    if marks >= 50:
        passed += 1
    else:
        failed += 1
    counter += 1

print(f'Number of passed students is: {passed}')
print(f'Number of failed students is: {failed}')