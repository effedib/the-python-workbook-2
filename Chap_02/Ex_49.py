# Chinese Zodiac

# Convert a year in its chinese zodiac animal

# Read the year from user
year = int(input("Enter the year: "))

# Compute the animal in chinese zodiac
if year % 12 == 8:
    chinese_zodiac = 'Dragon'
elif year % 12 == 9:
    chinese_zodiac = 'Snake'
elif year % 12 == 10:
    chinese_zodiac = 'Horse'
elif year % 12 == 11:
    chinese_zodiac = 'Sheep'
elif year % 12 == 0:
    chinese_zodiac = 'Monkey'
elif year % 12 == 1:
    chinese_zodiac = 'Rooster'
elif year % 12 == 2:
    chinese_zodiac = 'Dog'
elif year % 12 == 3:
    chinese_zodiac = 'Pig'
elif year % 12 == 4:
    chinese_zodiac = 'Rat'
elif year % 12 == 5:
    chinese_zodiac = 'Ox'
elif year % 12 == 6:
    chinese_zodiac = 'Tiger'
elif year % 12 == 7:
    chinese_zodiac = 'Hare'
else:
    chinese_zodiac = ''

# Report the result
if chinese_zodiac == '':
    print("Year invalid!")
else:
    print("{} is the year of {}".format(year, chinese_zodiac))