# Binary to Decimal

# Convert a binary (base 2) number to a decimal (base 10)

binary = input("Enter a binary number (base 2): ")

# Maybe the workbook wants a solution like this
reversed_binary = ""
for i in binary[::-1]:
    reversed_binary += i

counter = 0
decimal = 0
for i in reversed_binary:
    if i == '1':
        n = 2 ** counter
        decimal += n
    counter += 1
print("Basic Style:  The decimal of {} is {}".format(binary, decimal))


# My preferred solution
reversed_binary = ""
decimal = 0
for i in reversed(binary):
    reversed_binary += i

for c, i in enumerate(reversed_binary):
    if i == '1':
        decimal += (2 ** c)
print("Professional Style:  The decimal of {} is {}".format(binary, decimal))