# Write a programme to find sum of natural numbers whose start and end are given

start_num = int(input('Enter start number: '))
last_num = int(input('Enter last number: '))

sum = 0.5*(start_num + last_num)*(last_num - start_num + 1 )

print(f'Sum between numbers from {start_num} to {last_num} is: {sum}')