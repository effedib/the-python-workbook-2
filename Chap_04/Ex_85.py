# Compute the hypotenuse

# This function takes the lengths of the two shorter sides of a right triangle as its parameters and returns the hypotenuse computed using the Pythagorean theorem.

def hypotenuse(side1: float, side2: float) -> float:
    from math import sqrt
    
    hyp = sqrt(side1 ** 2 + side2 ** 2)

    return hyp

def main():
    cateto1     = float(input("Enter the first shorter side: "))
    cateto2     = float(input("Enter the second shorter side: "))
    ipotenusa   = hypotenuse(cateto1, cateto2)   
    print("The hypotenuse of this triangle is {:.2f}".format(ipotenusa))

if __name__ == "__main__":
    main()