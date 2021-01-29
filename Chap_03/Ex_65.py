# Temperature Conversion Table

# Display a temperature conversion table for
# degrees Celsius and degrees Fahrenheit

for celsius in range(0, 100, 10):
    farhenheit = (celsius * 9 / 5) + 32
    print("Celsius: {:2d} - Farhenheit: {:6.2f}".format(celsius, farhenheit))