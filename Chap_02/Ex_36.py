# Dog Years

# Conversion years human/dog
FIRST_YEARS = 10.5
ADULT_YEARS = 7

# Read the dog age from user
age = float(input("Digit how old is the dog: "))

# Analyse and display the equivalent human age
if age <= 0:
    print("Invalid number!")
elif age > 0 and age <= 2:
    print("Equivalent human age: " + str(age * FIRST_YEARS))
else:
    adult = age - 2
    young = age - adult
    print("Equivalent human age: " + str((young * FIRST_YEARS) + (adult * ADULT_YEARS)))