# Below and Above Average

# Read a list of numbers from the user, display the average, all of the below and above average values.

# Read the numbers from user and create a list
num = input("Enter the first number: ")

list_num = []
while num != '':
    list_num.append(float(num))
    num = input("Enter the next number (blank to quit): ")

# Compute average and create 3 lists for below, equal and above average
avg = sum(list_num) / len(list_num)
list_below = []
list_avg = []
list_above = []
for i in list_num:
    if i < avg:
        list_below.append(i)
    elif i == avg:
        list_avg.append(i)
    elif i > avg:
        list_above.append(i)

# Display results with appropriate labels
print("\nAverage of the entered values = {:.2f}\n".format(avg))

print("Values below average:")
for i in sorted(list_below):
    if list_below.index(i) == len(list_below) - 1:
        print(i, "\n")
    else:
        print(i, end=' ')

if avg in sorted(list_avg):
    print("Values in average:")
    for i in list_avg:
        if list_avg.index(i) == len(list_avg) - 1:
            print(i, "\n")
        else:
            print(i, end=' ')

print("Values above average:")
for i in sorted(list_above):
    if list_above.index(i) == len(list_above) - 1:
        print(i, "\n")
    else:
        print(i, end=' ')
