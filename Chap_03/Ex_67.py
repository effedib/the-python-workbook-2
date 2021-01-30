# Compute the Perimeter of a Polygon

# Compute the perimeter of polygon beginning by reading the coordinates of each point from the user

from math import sqrt

# Store the perimeter
perimeter = 0

# Read the firs coordinates from the user
first_x = float(input("Enter the first x-coordinate: "))
first_y = float(input("Enter the first y-coordinate: "))

# Assign the first values to x_prev ann y_prev
x_prev = first_x
y_prev = first_y

# Read the others coordinates
x = input("Enter the next x-coordinate (blank to quit): ")
while x != "":
    y = input("Enter the next y-coordinate: ")

    # Compute the distance to the previous point with Pythagorean theorem
    dist = sqrt(((float(x) - x_prev) ** 2) + ((float(y) - y_prev) ** 2))

    # Add the distance to the perimeter
    perimeter += dist

    # Set prev_coordinates for the next loop
    x_prev = float(x)
    y_prev = float(y)

    # Read the next x to check if the loop ended
    x = input("Enter the next x-coordinate (blank to quit): ")

# Compute the distance to the first point and add it to the perimeter
dist = sqrt(((x_prev - first_x) ** 2) + (y_prev - first_y) ** 2)
perimeter += dist

# Display the result
print("The perimeter of that polygon is {:.2f}".format(dist))