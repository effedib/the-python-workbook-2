# Next Prime

# This function finds and returns the first prime number larger than some integer, n.

def nextPrime(num: int):
    from Ex_98 import isPrime

    prime_num = num + 1
    while isPrime(prime_num) is False:
        prime_num += 1

    return prime_num

def main():
    number = int(input("Enter a non negative number: "))
    print("The next prime number after {:d} is {:d}.".format(number, nextPrime(number)))

if __name__ == "__main__":
    main()
