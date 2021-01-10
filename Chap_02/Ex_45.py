# Date to Holiday Name

# Convert an holiday date to its name

NEW_YEAR = 'January 1'
CANADA_DAY = 'July 1'
CHRISTMAS = 'December 25'

# Read the date from the user
holiday = input("Enter the date: ")

# Find the holiday name (if any)
if holiday == NEW_YEAR:
    holiday_name = 'New Year\'s Day'
elif holiday == CANADA_DAY:
    holiday_name = 'Canada Day'
elif holiday == CHRISTMAS:
    holiday_name = 'Christmas Day'
else:
    holiday_name = ''

# Display the result
if holiday_name == '':
    print("The entered date doesn't correspond to a fixed-date holiday")
else:
    print("The holiday found is: \"{:s}\"".format(holiday_name))