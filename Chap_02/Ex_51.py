# Roots of a Quadratic Function

# Compute the real root of a quadratic function (if any)

# Import math module so we can use the sqrt function
from math import sqrt

# Read a b c from user
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

# Compute the discriminant of the function
discriminant = b**2 - 4*a*c

# Compute the roots and display the result
if discriminant < 0:
    print("This quadratic function has no real roots")
elif discriminant == 0:
    root_plus = -b / (2 * a)
    print("This quadratic function has one real root: {:.2f}".format(root_plus))
else:
    root_plus = (-b +sqrt(discriminant)) / (2 * a)
    root_minus = (-b -sqrt(discriminant)) / (2 * a)
    print("This quadratic function has two real roots: {:.2f} and {:.2f}".format(root_plus, root_minus))