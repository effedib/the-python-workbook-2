# Compound interest

# Read the amount deposited from user
money_deposited = float(input("How much did you deposit? $"))

# Display the amount in the savings account after 1, 2 and 3 years
for years in range(1, 4):
    money_deposited = money_deposited + (money_deposited * 0.04)
    print("Year: %i. Amount in the savings account: $%.2f" % (years, money_deposited))