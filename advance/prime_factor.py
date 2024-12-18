"""Implement a function that takes a natural number as an argument and returns a list containing the prime factorization of that number.
  Present the solution in the form of a function called calculate().
"""
# [IN]: calculate(48)
# [OUT]: [2, 2, 2, 2, 3]

num = int(input())

result = []
c = 2

while num >= c:
    if num%c == 0:
        result.append(c)
        num = num//c
    else:
        c = c+1



print(result)

