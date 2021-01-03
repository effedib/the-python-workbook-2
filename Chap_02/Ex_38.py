# Name That Shape

# Read  the number of sides from the user
sides = int(input("Enter the number of sides of the shape: "))

# Find the shape or leaving it empty if is entered a wrong number of sides
shape = ""
if sides == 3:
    shape = "triangle"
elif sides == 4:
    shape = "square"
elif sides == 5:
    shape = "pentagon"
elif sides == 6:
    shape = "hexagon"
elif sides == 7:
    shape = "heptagon"
elif sides == 8:
    shape = "octagon"
elif sides == 9:
    shape = "nonagon"
elif sides == 10:
    shape = "decagon"

# Display an error message if is a wrong value or the name of the polygon
elif sides > 10:
    print("The numer of sides is greater than allowed")
else:
    print("Value not allowed")

if sides in [3,4,5,9,10]:
    print("The shape is a " + shape)
elif sides in [6,7,8]:
    print("The shape is an " + shape)