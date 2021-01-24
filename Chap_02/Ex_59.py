# Next Day

# Read a date from the user and computes its immediate successor

# Read the date from the user
year, month, day = input("Enter the date in this format YYYY-MM-DD: ").split("-")
year, month, day = (int(year), int(month), int(day))
date = "{}-{:02d}-{:02d}".format(year, month, day)

# Leap year control
if (year % 400) == 0:
    isLeap = True
elif (year % 100) == 0:
    isLeap = False
elif (year % 4) == 0:
    isLeap = True
else:
    isLeap = False

# Analyse the date
if month == 12 and day == 31:

    day = 1
    month = 1
    year += 1

elif day == 31 or\
    (day == 30 and month in [4, 6, 9, 11]) or \
    (day == 28 and month == 2 and isLeap is False) or\
    (day == 29 and month == 2 and isLeap is True):

    day = 1
    month += 1

else:

    day += 1

# Display the result
print("The day immediately after {} is {}-{:02d}-{:02d}".format(date, year, month, day))