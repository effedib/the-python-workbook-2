# Ordinal Date to Gregorian Date

# This function takes an ordinal date as its parameter (year and day) and returns the day and month corresponding to that ordinal date

# Non sono riuscito a risolverlo

""" from Ex_91 import isLeap

J = 105 + (365*2020)

y = 4716
v = 3
j = 1401
u = 5
m = 2
s = 153
n = 12
w = 2
r = 4
B = 274277
p = 1461
C = -38

f = J + j + (((4 * J + B) // 146097) * 3) // 4 + C
e = r * f + v
g = (e % p) // r
h = u * g + w
D = (h % s) // u + 1
M = ((h // s + m) % n) + 1
Y = (e // p) - y + (n + m - M) // n

print("{}-{}-{}".format(D, M, Y)) """