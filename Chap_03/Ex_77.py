# Multiplication Table

# Create a multiplication table that shows the products of all combinations of integer including 10 times 10.

# My solution

for i in range(11):
    if i != 0:
        print("%3d" % i, " ", end="")
    for n in range(11):
        if i == 0 and n == 0:
            print("%3s" % "", " ", end="")
        elif i == 0 and n != 0:
            print("%3d" % (n+i), " ", end="")
        elif i != 0 and n == 0:
            pass
        else:
            print("%3d" % (n*i), " ", end="")
    print("\n")

# ---------------------------------------------------------------- #


# Workbook solution

print("    ", end="")
for i in range(1,11):
    print("%4d" % i, end="")
print()

for i in range(1, 11):
    print("%4d" % i, end="")
    for j in range(1, 11):
        print("%4d" % (i * j), end="")
    print()