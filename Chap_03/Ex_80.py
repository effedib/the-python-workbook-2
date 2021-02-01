# Prime Factors

# Read an integer n from the user and compute the prime numbers that can be multiplied together to compute n

n = int(input("Enter an integer (2 or greater): "))

factor = 2

if n <= 2:
    print("Only integer greater than or equal to 2 allowed!")
else:
    print("The prime factors of {} are:".format(n))
    while factor <= n:
        if n % factor == 0:
            n //= factor
            print(factor)
        else:
            factor += 1