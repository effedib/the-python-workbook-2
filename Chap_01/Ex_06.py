# Tax and Tip

# Compute tax and tip based on the cost of a meal oredered at restaurant

# Conversion rate
TAX_RATE = 0.22
TIP_RATE = 0.18

# Read the cost of the meal
meal = float(input("How much for the meal? "))

# Compute tax, tip and total
tax = (meal * TAX_RATE)
tip = (meal * TIP_RATE)
total = (meal + tax + tip)

# My Display output
# print("Tax: $%.2f" % tax)
# print("Tip: $%.2f" % tip)
# print("Total: $%.2f" % total)

# Workbook output
print("The tax is $%.2f and the tip is $%.2f, \
making the total $%.2f." % (tax, tip, total))