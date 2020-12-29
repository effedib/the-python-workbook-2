# Sum of the Digits in an Integer

num = input("Inserisci un numero di 4 cifre: ")

a, b, c, d = [num[0], num[1], num[2], num[3]]
a, b, c, d = [int(a), int(b), int(c), int(d)]
print(a, "+", b, "+", c, "+", d, "=", a+b+c+d)