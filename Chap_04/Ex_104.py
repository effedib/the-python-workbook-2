# Hexadecimal and Decimal Digits

# This functions convert hexadecimal to decimal and reverse.

def hex2int(hexadecimal: str) -> int:
    
    if hexadecimal.isdigit():
        
        return hexadecimal
    
    elif hexadecimal.isalpha():
        if 'A' <= hexadecimal.upper() <= 'F':
            
            return int(hexadecimal.upper(), base=16)

        else:

            return "Incorrect hexadecimal number"

def int2hex(dec: int) -> int or str:

    from Ex_96 import isInteger
    
    conversion = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

    if isInteger(dec):

        if 9 < int(dec) < 16:

            return conversion[int(dec)]
        
        elif 0 <= int(dec) <= 9:

            return dec

    return "Incorrect decimal number"

def main():
    print(hex2int('a'))
    print(int2hex('15'))

if __name__ == "__main__":
    main()