# Wisgets and gizmos

# Products cost in grams
WIDGET = 75
GIZMO = 112

# Read the number of widgets and gizmos  from user
num_widgets = int(input("How many widgets? "))
num_gizmos = int(input("How many gizmos? "))

# Compute total weight in kg
tot_weight = (num_gizmos * GIZMO + num_widgets * WIDGET) / 1000

# Display the results
print("Total weight: %.2f kg" % tot_weight)