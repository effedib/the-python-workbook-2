# Distance units

# Conversion rate feet to inches, yards and miles
INCHES = 12
YARDS = 0.333333
MILES = 0.000189394

# Read measurement in feet from user
feet = float(input("Enter measurement in feet: "))

# Compute the conversion and display the results
print("Inches: %.2f" % (feet * INCHES))
print("Yards: %.2f" % (feet * YARDS))
print("Miles: %.2f" % (feet * MILES))