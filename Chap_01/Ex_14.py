# Height Units

# Conversion rate
FOOT = 12       # 1 foot = 12 inches
INCH = 2.54     # 1 inch = 2.54 centimeters

# Read height in feet and inches from user
feet = int(input("Height in feet: "))
inches = int(input("Add the number of inches: "))

# Compute the conversion in centimeters
cm = (((feet * FOOT) + inches) * INCH)

# Display the result
print("Height in centimeters: %.2f" % cm)