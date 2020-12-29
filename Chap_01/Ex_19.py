# Free fall

import math

# Constant of acceleration due to gravity
GRAVITY = 9.8

# Read the height from witch the object is dropped from user
height = float(input("Inserire l'altezza in metri: "))

# Compute final speed
velocita_finale = math.sqrt(2 * height * GRAVITY)

# Display the result
print("Velocità al momento dell'impatto: %.2f m/s" % velocita_finale)