"""
Compound Interest Equation
A = P(1 + r/n)nt

Where:
A = Accrued Amount (principal + interest)
P = Principal Amount
I = Interest Amount
R = Annual Nominal Interest Rate in percent
r = Annual Nominal Interest Rate as a decimal
r = R/100
t = Time Involved in years, 0.5 years is calculated as 6 months, etc.
n = number of compounding periods per unit t; at the END of each period
"""

# principal_amount = 10000
# rate = 3.875
# n = 12
# t = 7.5

principal_amount = float(input("Principal : "))
rate = float(input("Rate : "))
n = float(input("Compound : "))
t = float(input("Time : "))

print("Calculating the compound interest ....")
accrual = principal_amount * (1.0 + ((rate / 100) / n)) ** (n * t)
print("The final amount after", t, "years is", round(accrual, 2))
