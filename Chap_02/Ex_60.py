# What Day of the Week Is January 1?

# Report the of the week for January 1 of a given year

from math import floor
from datetime import datetime as dt

# Check the current year
today = dt.now()                        # now() represents the current date
this_year = dt.strftime(today, "%Y")    # strftime() extract a part of a date, in this case the year
this_year = int(this_year)

# Days of the week
day_week = {
    0: "Sunday",
    1: "Monday",
    2: "Thuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday"
}

# Read the year from the user
year = int(input("Enter the year: "))

# Calculate the day
day = (year + floor((year - 1) / 4) - floor((year - 1) / 100) + floor((year - 1) / 400)) % 7

# Display the result
if year - this_year < 0:
    print("In the year {}, January 1 was fallen on a {}".format(year, day_week[day]))
else:
    print("For the year {}, January 1 will fall on a {}".format(year, day_week[day]))