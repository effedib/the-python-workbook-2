# List of Proper Divisors

# This function computes all of the proper divisors of a positive integer and returns a list that contains all
# of this values.

def properDivisors(n: int) -> list:

    # empty list for proper divisors
    proper_divisors = []

    # append all of the int less than n with module == 0
    for i in range(1, n):
        if n % i == 0:
            proper_divisors.append(i)

    return proper_divisors


def main():

    num = int(input("Enter an integer: "))
    print("The proper divisors for {} are:".format(num))
    prop_div = properDivisors(num)
    for i in prop_div:
        print(i, end=' ')


if __name__ == "__main__":
    main()