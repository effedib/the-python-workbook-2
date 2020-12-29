# Distance between two points on Earth

import math

# Read the latitude and longitude of two points on Earth in degrees
lat1, long1 = input("Digitare le coordinate del 1° punto in gradi: ").split() # se si usa il metodo plit viene registratta automaticamente una stringa occorre convertirla dopo
lat2, long2 = input("Digitare le coordinate del 2° punto in gradi: ").split()

# Conversion in integers and radians
lat1, lat2 = [int(lat1), int(lat2)]
lat1, lat2 = [math.radians(lat1), math.radians(lat2)]
long1, long2 = [int(long1), int(long2)]
long1, long2 = [math.radians(long1), math.radians(long2)]

# Compute distance and display the results
distance = 6371.01 * math.acos(math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * math.cos(long1 - long2))
print("Distanza: %.2f" % distance)