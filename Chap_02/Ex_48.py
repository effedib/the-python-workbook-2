# Birth Date to Astrological Sign

# Convert a birth date into its zodiac sign

# Read the date from user
birth_month = input("Enter your month of birth: ").lower()
birth_day = int(input("Enter your day of birth: "))

# Find the zodiac sign
if (birth_month == 'december' and birth_day >= 22) or (birth_month == 'january' and birth_day <= 19):
    zodiac = 'Capricorn'
elif (birth_month == 'january' and birth_day >= 20) or (birth_month == 'february' and birth_day <= 18):
    zodiac = 'Aquarius'
elif (birth_month == 'february' and birth_day >= 19) or (birth_month == 'march' and birth_day <= 20):
    zodiac = 'Pisces'
elif (birth_month == 'march' and birth_day >= 21) or (birth_month == 'april' and birth_day <= 19):
    zodiac = 'Aries'
elif (birth_month == 'april' and birth_day >= 20) or (birth_month == 'may' and birth_day <= 20):
    zodiac = 'Taurus'
elif (birth_month == 'may' and birth_day >= 21) or (birth_month == 'june' and birth_day <= 20):
    zodiac = 'Gemini'
elif (birth_month == 'june' and birth_day >= 21) or (birth_month == 'july' and birth_day <= 22):
    zodiac = 'Cancer'
elif (birth_month == 'july' and birth_day >= 23) or (birth_month == 'august' and birth_day <= 22):
    zodiac = 'Leo'
elif (birth_month == 'august' and birth_day >= 23) or (birth_month == 'september' and birth_day <= 22):
    zodiac = 'Virgo'
elif (birth_month == 'september' and birth_day >= 23) or (birth_month == 'october' and birth_day <= 22):
    zodiac = 'Libra'
elif (birth_month == 'october' and birth_day >= 23) or (birth_month == 'november' and birth_day <= 21):
    zodiac = 'Scorpio'
elif (birth_month == 'november' and birth_day >= 22) or (birth_month == 'december' and birth_day <= 21):
    zodiac = 'Sagittarius'
else:
    zodiac = ''

# Display the result
if zodiac == '':
    print("Invalid date!")
else:
    print("If your birthday is {} {}, your zodiac sign is: {}!".format(birth_month.capitalize(), birth_day, zodiac))