# Greatest Common Divisor
# This program uses Euclid's algorithm to determine the greatest common divisor of two integers entered by the user.


def euclide_commondivisor(a: int, b: int) -> int:
    if b == 0:

        return a

    else:
        c = a % b

        return euclide_commondivisor(b, c)


def main():
    num_a = int(input("Enter the first integer: "))
    num_b = int(input("Enter the second integer: "))
    print("The greatest common divisor of '{}' and '{}' is: {}".format(num_a, num_b,\
                                                                       euclide_commondivisor(num_a, num_b)))


if __name__ == '__main__':
    main()

