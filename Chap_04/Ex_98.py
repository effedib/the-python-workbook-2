# Is a Number Prime?

# This function determines whether or not its parameter is prime.

def isPrime(num: int) -> bool:

    if num <= 1:

        return False

    for i in range(2, num//2):
        
        if num % i == 0:
            
            return False

    return True

def main():
    num = int(input("Enter the number: "))
    if isPrime(num):
        print("{:d} is a prime number.".format(num))
    else:
        print("{:d} is not a prime number.".format(num))

if __name__ == "__main__":
    main()