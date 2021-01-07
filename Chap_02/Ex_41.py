# Classifying Triangles

# Classify and display a triangle's type based on the length of its sides

# Read the length of the sides from user
side1, side2, side3 = input('Enter the sides length: ').split()
side1, side2, side3 = [int(side1), int(side2), int(side3)]

# Match the length of the sides and display the triangle's type
if side1 == side2 == side3:
    print('Triangle\'s type: equilateral')
elif side1 != side2 != side3:
    print('Triangle\'s type: scalene')
else:
    print('Triangle\'s type: isoscele')