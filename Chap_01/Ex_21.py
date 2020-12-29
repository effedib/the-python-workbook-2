# Area of a Triangle (3 sides)

import math

# Read the sides from user
s1, s2, s3 = input("Inserisci i 3 lati: ").split()
s1,s2,s3 = [float(s1), float(s2), float(s3)]

# Compute the area
s = (s1 + s2 + s3) / 2
area = math.sqrt(s * (s - s1) * (s - s2) * (s - s3))

# Display the result
print("Area del triangolo: %.2f" % area)