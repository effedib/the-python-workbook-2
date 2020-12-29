# Area of a regular polygon

import math

# Read the length of a side and the number of the sides
length_sides, num_sides = input("Inserisci la lunghezza dei lati ed il loro numero \nseparati da uno spazio: ").split()
length_sides, num_sides = [float(length_sides), int(num_sides)]

# Compute the area of the polygon
area = (num_sides * (length_sides ** 2)) / (4 * math.tan(math.pi / num_sides))

# Display the result
print("Area del poligono: %.2f" % area)