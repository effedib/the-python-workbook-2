# Heat Capacity

# Read the mass of water and the temperature change
mass_water = float(input("Inserisci la quantità d'acqua in ml: "))
temperature = float(input("Inserisci il cambio di temperatura desiderato in gradi Celsius: "))

# Define constants for heat capacity and electricity costs
HEAT_CAPACITY = 4.186
ELEC_COST = 8.9 # cents
J_TO_KWH = 2.777e-7

# Compute energy needed
energy_needed = mass_water * temperature * HEAT_CAPACITY

# Conversion in kwh
kwh = energy_needed * J_TO_KWH

# Compute the cost of energy
cost = kwh * ELEC_COST

# Display the results
print("Energia necessaria: %d Joule" % energy_needed)
print("Costo riscaldamento acqua: %.2f cents" % cost)