# Celsius to Fahrenheit and Kelvin

# Conversion factor constants
FAH = 32
KEL = 273.15

# Read the temperature in degrees Celsius
degrees = float(input("Qual è la temperatura in gradi centigradi? "))

# Convert the temperature in Fahrenheit and Kelvin
fahren = degrees + FAH
kelvin = degrees + KEL

# Display the results
print("Temperatura in gradi Fahrenheit", fahren)
print("Temperatura in gradi Kelvin", kelvin)