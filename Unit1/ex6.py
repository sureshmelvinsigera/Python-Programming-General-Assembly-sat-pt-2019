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

principal_amount = 1000
n = 12
rate = 8
t = 12

print("Calculating the compound interest ....")
accrual = principal_amount * (1.0 + ((rate / 100) / n)) ** (n * t)
print("The final amount after", t, "years is", accrual)
