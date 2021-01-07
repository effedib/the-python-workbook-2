# Month Name to Number of Days

# Display the number of days of a month after reading that from user

# Read the month as string from the user
month = input("Enter the month: ").lower()
day = 0

# Evaluate what month is and how many days are
if month == 'february':
    year = input("The year is leap?(Y/N) ").lower()
    if year == 'y':
        day = 29
    else:
        day = 28
elif month in ['april', 'june', 'september', 'november']:
    day = 30
else:
    day = 31
print("Days of the month: {}".format(day))
        