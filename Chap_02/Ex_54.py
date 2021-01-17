# Assessing Employees

# Report the performance and the amount raised to an employee according to his rating

# Read the rating from user
rating = float(input("Enter your rating: "))

# Classify the performance
if rating == 0:
    performance = 'Unacceptable Performance'
elif rating == 0.4:
    performance = 'Acceptable Performance'
elif rating >= 0.6:
    performance = 'Meritorious Performance'
else:
    performance = ''

# Report the result
if performance == '':
    print("Rating not allowed")
else:
    earnings = rating * 2400
    print("Your rating is \"{:s}\" so the amount earned this year is {:.2f}".format(performance, earnings))