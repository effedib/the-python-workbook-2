# Roman Numerals

# This function converts a Roman numeral to an integer using recursion.


def roman2int(roman: str) -> int:

    romans_table = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'I': 1}

    roman = roman.upper()

    if roman == '':
        return 0

    if len(roman) > 1:
        if romans_table[roman[0]] < romans_table[roman[1]]:
            tot = romans_table[roman[1]] - romans_table[roman[0]]
            return tot + roman2int(roman[2:])

    tot = romans_table[roman[0]]

    return tot + roman2int(roman[1:])


def main():
    roman_num = input("Enter a roman number: ")
    print(roman2int(roman_num))


if __name__ == '__main__':
    main()
