num = int(input("Enter a number: "))
reversed_num = 0
while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    print(digit, reversed_num)
    num = num // 10
print("Reversed number is:", reversed_num)
