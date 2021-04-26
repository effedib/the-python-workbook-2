# Square Root

# Implements Newton's method to compute the square root of a number x

x = float(input('Enter the number to calculate the Square Root: '))
guess = x / 2

while abs((guess ** 2) - x) > (10 ** -12):
    guess = (guess + (x / guess)) / 2

print(guess)
