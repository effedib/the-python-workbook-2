# Wavelengths of Visible Light

# Commute the wavelength of visible light in its color

# Read the wavelength from the user
wavelength = float(input("Enter the wavelength: "))

# Classify the colors
if 380 <= wavelength < 450:
    color = 'violet'
elif 450 <= wavelength < 495:
    color = 'blue'
elif 495 <= wavelength < 570:
    color = 'green'
elif 570 <= wavelength < 590:
    color = 'yellow'
elif 590 <= wavelength < 620:
    color = 'orange'
elif 620 <= wavelength <= 750:
    color = 'red'
else:
    color = ''

# Display the result
if color == '':
    print("Invalid wavelength")
else:
    print("The color is {:s}".format(color))