# Volume of a Cylinder

from math import pi

# Read radius and height from user
radius = float(input("Inserire il raggio: "))
height = float(input("Inserire l'altezza: "))

# Compute base area and volume
area = pi * pow(radius, 2)
volume = area * height

# Display the result
print("Volume cilindro: %.1f" % volume)