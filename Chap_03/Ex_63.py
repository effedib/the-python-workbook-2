# Average

# Compute the average of a collection of values entered by the user

# Read the first value from the user
num = int(input("Enter an integer (0 to quit): "))

# Check if the first value is 0
if num != 0:
    sum_num = 0
    count = 0

    # Loop untile the 0 value is entered
    while num !=0:
        sum_num += num
        num = int(input("Enter an integer (0 to quit): "))
        count += 1
    
    # Print the result
    print("Average: {:.2f}".format(sum_num / count))

# Print the error if 0 is the first value
else:
    print("No number entered!")