# Decimal to Binary

# Convert a decimal (base 10) number to a binary (base 2) number

def dec2bin(original_decimal: int) -> str:

    decimal = original_decimal
    result = ''

    while decimal > 0:
        remainder = decimal % 2
        result = str(remainder) + result
        decimal //= 2

    return result


def main():
    num = int(input("Enter a decimal number (base 10): "))
    print("The binary of {} is {}".format(num, dec2bin(num)))


if __name__ == '__main__':
    main()
