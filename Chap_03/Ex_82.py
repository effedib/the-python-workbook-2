# Decimal to Binary

# # Convert a decimal (base 10) number to a binary (base 2) number

original_decimal = int(input("Enter a decimal number (base 10): "))

decimal = original_decimal
result = ''

while decimal > 0:
    remainder = decimal % 2
    result = str(remainder) + result
    decimal //= 2

print("The binary of {} is {}".format(original_decimal, result))