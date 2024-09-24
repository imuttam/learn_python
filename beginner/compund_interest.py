# Calculate compund interest from given data

P = float(input("Enter amount: "))
r = float(input("Enter rate of interest: "))
t = float(input("Enter time duration in year: "))

CI = P*(1+r/100)**t - P

print(f'Compund Interest on given amount is: {CI:.2f}')
