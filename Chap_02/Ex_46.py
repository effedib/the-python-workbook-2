# What Color Is That Square

# Find the color of a square on a chess board

# Read the position from the user
position = input("Enter the position: ").lower()

coloumn = position[0]
row = int(position[1])

# Find the color of the square on that position
if (coloumn in ['a','c','e','g'] and row % 2 == 0) or coloumn not in ['a','c','e','g'] and row % 2 != 0:
    square = 'white'
else:
    square = 'black'

# Display the result
print("The color of the square is: {:s}".format(square))