# This function say if a positive integer is perfect or not.

def is_perfectint(n: int) -> bool:
    from Ex_115 import properDivisors

    proper_list = properDivisors(n)  # list of all the n proper divisors

    if n == sum(proper_list):
        return True

    return False


def main():
    LIMIT = 10000
    print("The perfect numbers between 1 and {} are:".format(LIMIT))
    for i in range(1, LIMIT):
        if is_perfectint(i):
            print(i, end=' ')


if __name__ == "__main__":
    main()
