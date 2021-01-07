# Sound Levels

# Read a sound level in decibels from the user, match the level of noise and display the result

# Read the sound level in decibels
sound = int(input("Enter the sound level in decibels: "))

# Match level of noises and display the results
if sound == 130:
    print("Level: Jackhammer")
elif sound == 106:
    print("Level: Gas Lawnmower")
elif sound == 70:
    print("Level: Alarm Clock")
elif sound == 40:
    print("Level: Quiet Room")
elif 40 < sound < 70:
    print("Level between Quiet Room and Alarm Clock")
elif 70 < sound < 106:
    print("Level between Alarm Clock and Gas Lawnmower")
elif 106 < sound < 130:
    print("Level between Gas Lawnmower and Jackhammer")
elif sound > 130:
    print('The sound level is too high')
else:
    print('The sound level is too low')