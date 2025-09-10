# Prompt the user for their monthly income
monthly_income = float(input("Enter your monthly income: "))

# Prompt the user for their monthly expenses
monthly_expenses = float(input("Enter your monthly expenses: "))

# Calculate the monthly savings
monthly_savings = monthly_income - monthly_expenses

# annual interest rate
annual_interest_rate = 0.05

# Calculate projected savings
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * annual_interest_rate)

# Display the monthly and projected savings
print(f"Your monthly savings are: ${monthly_savings}")
print(f"Projected savings after one year, with interest, is: ${projected_savings}")
