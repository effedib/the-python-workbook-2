# Recursive Square Root

# Implements Newton's method to compute the square root of a number x, but using recursion instead of a loop.


def rec_sqr_root(num: float, guess: float = 1) -> float:
    a = abs((guess ** 2) - num)
    b = num * (10 ** (-12))

    if a <= b:

        return guess

    else:
        guess = (guess + (num / guess)) / 2

        return rec_sqr_root(num, guess)


def main():
    x = float(input('Enter the number to calculate the Square Root: '))
    print("The square root of {} is: {:.2f}".format(x, rec_sqr_root(x)))


if __name__ == "__main__":
    main()

