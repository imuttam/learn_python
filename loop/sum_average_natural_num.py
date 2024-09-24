# write a program to display sum and average of first n natural number.

n = int(input('Enter range of number: '))

count = 0
total = 0

while count < n:
    total += count
    count += 1

average = total/count

print(f'Sum of first {n} natural number is: {total}')
print(f'Average of first {n} natural number is: {average:.2f}')
