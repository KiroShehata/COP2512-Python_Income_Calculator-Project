income_value = float(input('Enter the income amount (in dollars): '))
tax_percentage = float(input('Enter the tax rate (in percent): '))
tax = tax_percentage / 100 #  = 0.165

tax_amount = income_value * tax # = 8,196
income_minus = income_value - tax_amount


print(f'The tax amount is: ${tax_amount:.2f}')
print(f'The income after tax is: ${income_minus:.2f}')