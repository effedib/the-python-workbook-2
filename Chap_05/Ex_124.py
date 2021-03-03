# Line of Best Fit

# Read the coordinates from user, than calculate the line of best fit using the formula "y = mx + b".

# Read the coordinates from user and append to two lists respectively for x and y.
x_num = input("Enter the first X coordinate: ")

x_list = []
y_list = []

while x_num != '':
    x_list.append(float(x_num))
    y_num = input("Enter the next Y coordinate: ")
    y_list.append(float(y_num))
    x_num = input("Enter the next X coordinate (blank to quit): ")

# The following steps are used to calculate m
# First compute the average of the values in the lists
x_avg = sum(x_list) / len(x_list)
y_avg = sum(y_list) / len(y_list)

# After we want to know the difference between every element of the list and the its average
x_diff = [i - x_avg for i in x_list]
y_diff = [i - y_avg for i in y_list]

# Then multiply every element of the x_diff by the equivalent of the y_diff
xy_list = [x_diff[i] * y_diff[i] for i in range(len(x_diff))]

# For the divisor we must square x_diff
x_diff_sqrt = [(i - x_avg) ** 2 for i in x_list]

# Now sum the xy_list and after sum the x_diff_sqrt
sum_xy = sum(xy_list)
sum_x_diff_sqrt = sum(x_diff_sqrt)

# Compute m and b
m = sum_xy / sum_x_diff_sqrt
b = y_avg - (m * x_avg)

# Display the result
print('y = {:.1f}x + {:.1f}'.format(m, b))
