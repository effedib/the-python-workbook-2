# Bottle deposits

# Conversion rate
LESS_LITER = 0.10
MORE_LITER = 0.25

# Read the number of containers from user
less_liter = int(input("How many containers until 1 liter? "))
more_liter = int(input("How many containers have more than 1 liter? "))

# Compute refund
refund = (less_liter * LESS_LITER) + (more_liter * MORE_LITER)

# Display the results
print("Prevision refund: $%.2f" % refund)