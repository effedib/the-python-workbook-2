# Units of Pressure

# Conversion constants
POUNDS_PER_SQUARE = 0.145038
MM_OF_MERCURY = 7.50062
ATMOSPHERE = 0.00986923

# Read the pressure in kilopascals
pascal = float(input("Inserisci la pressione in kilopascals: "))

# Compute the equivalent pressure
pounds_square = pascal * POUNDS_PER_SQUARE
mm_mercury = pascal * MM_OF_MERCURY
atmos = pascal * ATMOSPHERE

# Display the results
print("La pressione in libbre per pollice quadrato è: %.2f" % pounds_square)
print("La pressione in millimetri di mercurio è: %.2f" % mm_mercury)
print("La pressione in atmosfere è: %.2f" % atmos)