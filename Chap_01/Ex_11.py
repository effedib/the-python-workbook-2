# Fuel Efficiency

# Conversion rate
LKM = 235.215

# Read the miles-per-gallon from user
mpg = int(input("How many miles-per-gallon? "))

# Conversion from LPG to L/100km
lkm = LKM / mpg

# Display the results
print("Equivalent in L/100km: %.2f" % lkm)