# Frequency to Name

# Read the frequency from user
frequency = int(input('Insert a radiation frequency: '))

# Classify the frequency
if  3*(10**9) < frequency:
    wave = 'radio waves'
elif 3*(10**9) <= frequency < 3*(10**12):
    wave = 'microwaves'
elif 3 * (10 ** 12) <= frequency < 4.3 * (10 ** 14):
    wave = 'infrared light'
elif 4.3 * (10 ** 14) <= frequency < 7.5 * (10 ** 14):
    wave = 'visible light'
elif 7.5 * (10 ** 14) <= frequency < 3 * (10 ** 17):
    wave = 'ultraviolet light'
elif 3 * (10 ** 17) <= frequency < 3 * (10 ** 19):
    wave = 'X-Rays'
elif frequency > 3 * (10 ** 19):
    wave = 'Gamma Rays'

# Diplay the result
print("Radiation level: ", wave)