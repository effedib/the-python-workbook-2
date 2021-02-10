# Arbitrary Base Conversion

# This function converts a number from one base to another base

from Ex_104 import int2hex, hex2int

def binary2decimal(binary: str) -> int:
    reversed_binary = ""
    decimal = 0
    for i in reversed(str(binary)):
        reversed_binary += i

    for c, i in enumerate(reversed_binary):
        if i == '1':
            decimal += (2 ** c)
    
    return decimal

def decimal2binary(decimal: int) -> int:
    binary = ''
    while decimal > 0:
        remainder = decimal % 2
        binary = str(remainder) + binary
        decimal //= 2

    return binary

def baseconvert(number, new_base = 10, base_orig = 10):

    if new_base == 2:

        return decimal2binary(number)
    
    elif new_base == 16:

        return int2hex(number)
    
    elif new_base == 10:
        
        if base_orig == 2:

            return binary2decimal(number)

        elif base_orig == 16:

            return hex2int(number)
        
    else:

        return "Incorrect base number"



print(binary2decimal(10101))
print(decimal2binary(21))
print(hex2int('a'))
print(int2hex('15'))

print(baseconvert(10101, 10, 2))
print(baseconvert(21, 12))
print(baseconvert('a', 10, 16))
print(baseconvert('15', 16))