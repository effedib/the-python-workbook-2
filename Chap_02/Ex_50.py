# Richter Scale

# Report the descriptor of a earthquake according to its magnitude

# Read the magnitude from the user
magnitude = float(input("Enter the earthquake magnitude: "))

# Determine the range on the Richter scale
if magnitude < 2:
    earthquake = 'micro'
elif 2 <= magnitude < 3:
    earthquake = 'very minor'
elif 3 <= magnitude < 4:
    earthquake = 'minor'
elif 4 <= magnitude < 5:
    earthquake = 'light'
elif 5 <= magnitude < 6:
    earthquake = 'moderate'
elif 6 <= magnitude < 7:
    earthquake = 'strong'
elif 7 <= magnitude < 8:
    earthquake = 'major'
elif 8 <= magnitude < 10:
    earthquake = 'great'
else:
    earthquake = 'meteoric'

# Report the result
print("{:.2f} earthquake is considered to be a {:s} earthquake".format(magnitude, earthquake))