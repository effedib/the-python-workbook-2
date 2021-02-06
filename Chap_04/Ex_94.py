# Is It a Valid Triangle?

# This function determines whether or not three lengths can form a triangle

def isTriangle(side1: float, side2: float, side3: float) -> bool:
    from Ex_88 import Median

    if side1 == 0 or side2 == 0 or side3 == 0:
        
        return False
    
    if max(side1, side2, side3) >= (min(side1, side2, side3) + Median(side1, side2, side3)):
        
        return False
    else:
        
        return True

def main():
    lato1 = float(input("Enter the first lenght: "))
    lato2 = float(input("Enter the second lenght: "))
    lato3 = float(input("Enter the third lenght: "))
    triangle = isTriangle(lato1, lato2, lato3)
    if triangle is True:
        print("You can form a triangle!")
    else:
        print("A triangle cannot be formed")

if __name__ == "__main__":
    main()