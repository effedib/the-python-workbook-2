# Season from Month and Day

# Associate a date to the respective season

SPRING_MONTH = "march"
SPRING_DAY = 20
SUMMER_MONTH = 'june'
SUMMER_DAY = 21
FALL_MONTH = 'september'
FALL_DAY = 22
WINTER_MONTH = 'december'
WINTER_DAY = 21

# Read the date from the user
month = input("Enter the month: ").lower()
day = int(input("Enter the day: "))

# Find the season
if month == 'april' or month == 'may' or\
   (month == SPRING_MONTH and day >= SPRING_DAY) or (month == SUMMER_MONTH and day <SUMMER_DAY):
    season = 'Spring'
elif month == 'july' or month == 'august' or\
   (month == SUMMER_MONTH and day >= SUMMER_DAY) or (month == FALL_MONTH and day < FALL_DAY):
    season = 'Summer'
elif month == 'october' or month == 'november' or\
   (month == FALL_MONTH and day >= FALL_DAY) or (month == WINTER_MONTH and day < WINTER_DAY):
    season = 'Fall'
else:
    season = 'Winter'

# Display the result
print("{:s} {:d} is in {:s}".format(month.capitalize(), day, season))
