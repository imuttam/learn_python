# To check user eligibility to vote

age = int(input('Enter your age: '))

if age >= 18:
    print('You are eligible to vote.')

else:
    elig = 18-age
    print(f'You will be able to vote after {elig} years.')