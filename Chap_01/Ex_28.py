# Body Mass Index

# Read height ed weight from user
height, weight = input("Inserisci l'altezza in metri ed il peso in kg: ").split()

# Convert the variables from string to float
height, weight = [float(height), float(weight)]

# Compute the BMI
bmi = weight / (height * height)

# Display the result
print("Il tuo indice di massa corperea è: %.2f" % bmi)