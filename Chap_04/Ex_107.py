# Reduce a Fraction to Lowest Terms

# This function takes two integers that represent the numerator and denominator of a fraction as its only parameters and returns the fraction reduced to lowest terms as its result.

def maximDivisor(n: int, m: int) -> int:

    divisor = min(n, m)

    while n % divisor != 0 or m % divisor != 0:
        divisor -= 1
   
    return divisor

def reduceFraction(numerator: int, denominator: int) -> int:
    if numerator == 0:
        return (0,1)
    
    divisor = maximDivisor(numerator, denominator)

    return (numerator // divisor, denominator // divisor)

def main():
    num   = int(input("Enter the numerator of the function: "))
    denom = int(input("Enter the denominator of the function: "))

    new_num, new_denom = reduceFraction(num, denom)
    print("Here is the fraction reduced to lowest terms: {:d}/{:d}".format(new_num, new_denom))

if __name__ == "__main__":
    main()