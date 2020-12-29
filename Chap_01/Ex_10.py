# Arithmetic

import math

# Read a and b from user
a = int(input("Inserisci il valore di a: "))
b = int(input("Inserisci il valore di b: "))

# Compute and display the results
print(a, " + ", b, " = ", (a + b))
print(a, " - ", b, " = ", (a - b))
print(a, " * ", b, " = ", (a * b))
print(a, " / ", b, " = %.2f" % (a / b))
print(a, " % ", b, " = ", (a % b))
print("The base 10 logarithm of ", a, " = %.2f" % math.log10(a))
print(a, " ^ ", b, " = ", (a ** b))