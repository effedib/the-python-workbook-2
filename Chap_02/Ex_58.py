# Is It a Leap Year

# Determine if a given year is a leap year

# Read the year from the user
year = int(input("Enter the year: "))

# Calculate if it's a leap year and display the result
""" if (year % 400) == 0:
    print("The year {:d} is a leap year".format(year))
elif (year % 100) != 0:
    if (year % 4) == 0:
        print("The year {:d} is a leap year".format(year))
    else:
        print("The year {:d} isn\'t a leap year".format(year))
else:
    print("The year {:d} isn\'t a leap year".format(year)) """

# Workbook solution
if (year % 400) == 0:
    isLeap = True
elif (year % 100) == 0:
    isLeap = False
elif (year % 4) == 0:
    isLeap = True
else:
    isLeap = False

# Display the result
if isLeap:
    print("The year {:d} is a leap year".format(year))
else:
    print("The year {:d} isn\'t a leap year".format(year))