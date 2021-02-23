# Reverse Order
# Read integers from user and store them in a list, user 0 to mark the end of the list, display the values entered
# in reverse order with one value appearing on each line

# Read the first int from the user
num = int(input("Enter an integer (0 to quit): "))

# Create an empty list
list_int = []

# Loop to append integers into the list until 0 is entered
while num != 0:
    list_int.append(num)
    num = int(input("Enter another integer (0 to quit): "))

# Display the result in reversed order
for i in reversed(list_int):
    print(i)
