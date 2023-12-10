#!/usr/bin/env python3
print =("Tax Calci")
income = float(input("Enter the annual income: "));
print("Calculates tax on income based on 30%, 20%, 10% brackets respectively for 10L+, 8L+, 5L+")
print("Your income: ", income);
taxableIncome = income - 200000
tax = 0.0
taxBracket = 0.0
if income > 1000000:
  taxBracket = 30
elif income > 500000:
  taxBracket = 20
elif income > 300000:
  taxBracket = 10
else:
  print("Enter non zero income")

tax = taxableIncome * taxBracket/100

print("Computed Tax is ", tax, ". You are under taxBracket ", taxBracket, "%; your taxable income is ", taxableIncome)
print("In hand Income after Tax is ", income - tax)

