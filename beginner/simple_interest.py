# Calculate simple interest from given data

P = float(input("Enter amount: "))
r = float(input("Enter rate of interest: "))
t = float(input("Enter time duration in year: "))

SI = (P*r*t)/100

print(f'Simple interest on given amount is: {SI}')
print(f'Total amount after {t} year is: {P+SI}')