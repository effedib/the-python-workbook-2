# Greatest Common Divisor

# Read 2 positive integer and find their greatest common divisor

n = int(input("Enter the first positive integer: "))
m = int(input("Enter the first second integer: "))

d = min(n, m)

while n % d != 0 or m % d != 0:
    d -= 1
print("The greatest common divisor of {} and {} is {}".format(n, m, d))