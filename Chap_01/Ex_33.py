# Sort 3 Integers

a = int(input("Inserisci il primo numero: "))
b = int(input("Inserisci il secondo numero: "))
c = int(input("Inserisci il terzo numero: "))
minimum = min(a, b, c)
maximum = max(a, b, c)
medium = a + b + c - minimum - maximum
print(minimum)
print(medium)
print(maximum)