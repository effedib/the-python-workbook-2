import math

# Area circle and volume sphere

# Read the radius from user
raggio = float(input("Inserisci il raggio: "))

# Compute area and volume
area = math.pi * (raggio ** raggio)
volume = (4 / 3) * math.pi * pow(raggio, 3)

# Display the results
print("Area del cerchio: %.2f" % area)
print("Volume della sfera: %.2f" % volume)