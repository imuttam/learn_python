"""Find the sum of all numbers that are divisible by 5 or 7 less than 100."""

def calculate(num):
    result = []
    for number in range(1,100):
        if number%5 == 0 or number%7 == 0:
            result.append(number)

    return sum(result)

print(calculate(100))