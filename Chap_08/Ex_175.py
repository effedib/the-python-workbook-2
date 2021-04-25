# Recursive Decimal to Binary

# Convert a decimal (base 10) number to a binary (base 2) number using recursion

from Chap_03.Ex_82 import dec2bin


def rec_dec2bin(original_decimal: int) -> str:

    if original_decimal < 0:

        raise ValueError('You must enter a non-negative integer')

    if original_decimal == 0 or original_decimal == 1:

        return str(original_decimal)

    else:
        remainder = original_decimal % 2

        return rec_dec2bin((original_decimal // 2)) + str(remainder)


def main():
    num = int(input("Enter a decimal number (base 10): "))
    print("The binary of {} with a 'while' loop is: {}".format(num, dec2bin(num)))
    print("The binary of {} with recursion is: {}".format(num, rec_dec2bin(num)))


if __name__ == '__main__':
    main()

