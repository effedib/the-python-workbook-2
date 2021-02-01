# The Collatz Conjecture

# Read an integer n from the user and reports all of the values according to the Collatz Conjecture and ending with 1

n = int(input("Enter any positive integer: "))

while n > 0:
    while n > 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = n * 3 + 1
        print(n, end=" ")
    n = int(input("\nEnter another integer (0 or less to quit): "))