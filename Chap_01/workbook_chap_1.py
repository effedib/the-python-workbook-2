import math
""" # Tax and Tip

# Compute tax and tip based on the cost of a meal oredered at restaurant

# Conversion rate
TAX_RATE = 0.22
TIP_RATE = 0.18

# Read the cost of the meal
meal = float(input("How much for the meal? "))

# Compute tax, tip and total
tax = (meal * TAX_RATE)
tip = (meal * TIP_RATE)
total = (meal + tax + tip)

# My Display output
# print("Tax: $%.2f" % tax)
# print("Tip: $%.2f" % tip)
# print("Total: $%.2f" % total)

# Workbook output
print("The tax is $%.2f and the tip is $%.2f, \
making the total $%.2f." % (tax, tip, total)) """

""" # Sum of the first n positive integers

n = int(input())
somma = (n * (n + 1)) / 2
print(somma) """

""" # Wisgets and gizmos

# Products cost in grams
WIDGET = 75
GIZMO = 112

# Read the number of widgets and gizmos  from user
num_widgets = int(input("How many widgets? "))
num_gizmos = int(input("How many gizmos? "))

# Compute total weight in kg
tot_weight = (num_gizmos * GIZMO + num_widgets * WIDGET) / 1000

# Display the results
print("Total weight: %.2f kg" % tot_weight) """

""" # Compound interest

# Read the amount deposited from user
money_deposited = float(input("How much did you deposit? $"))

# Display the amount in the savings account after 1, 2 and 3 years
for years in range(1, 4):
    money_deposited = money_deposited + (money_deposited * 0.04)
    print("Year: %i. Amount in the savings account: $%.2f" % (years, money_deposited)) """

""" # Arithmetic

# Read a and b from user
a = int(input("Inserisci il valore di a: "))
b = int(input("Inserisci il valore di b: "))

# Compute and display the results
print(a, " + ", b, " = ", (a + b))
print(a, " - ", b, " = ", (a - b))
print(a, " * ", b, " = ", (a * b))
print(a, " / ", b, " = %.2f" % (a / b))
print(a, " % ", b, " = ", (a % b))
print("The base 10 logarithm of ", a, " = %.2f" % math.log10(a))
print(a, " ^ ", b, " = ", (a ** b)) """

""" # Fuel Efficiency

# Conversion rate
LKM = 235.215

# Read the miles-per-gallon from user
mpg = int(input("How many miles-per-gallon? "))

# Conversion from LPG to L/100km
lkm = LKM / mpg

# Display the results
print("Equivalent in L/100km: %.2f" % lkm) """

""" # Distance between two points on Earth

# Read the latitude and longitude of two points on Earth in degrees
lat1, long1 = input("Digitare le coordinate del 1° punto in gradi: ").split() # se si usa il metodo plit viene registratta automaticamente una stringa occorre convertirla dopo
lat2, long2 = input("Digitare le coordinate del 2° punto in gradi: ").split()

# Conversion in integers and radians
lat1, lat2 = [int(lat1), int(lat2)]
lat1, lat2 = [math.radians(lat1), math.radians(lat2)]
long1, long2 = [int(long1), int(long2)]
long1, long2 = [math.radians(long1), math.radians(long2)]

# Compute distance and display the results
distance = 6371.01 * math.acos(math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * math.cos(long1 - long2))
print("Distanza: %.2f" % distance) """


""" # Height Units

# Conversion rate
FOOT = 12       # 1 foot = 12 inches
INCH = 2.54     # 1 inch = 2.54 centimeters

# Read height in feet and inches from user
feet = int(input("Height in feet: "))
inches = int(input("Add the number of inches: "))

# Compute the conversion in centimeters
cm = (((feet * FOOT) + inches) * INCH)

# Display the result
print("Height in centimeters: %.2f" % cm) """

""" # Distance units

# Conversion rate feet to inches, yards and miles
INCHES = 12
YARDS = 0.333333
MILES = 0.000189394

# Read measurement in feet from user
feet = float(input("Enter measurement in feet: "))

# Compute the conversion and display the results
print("Inches: %.2f" % (feet * INCHES))
print("Yards: %.2f" % (feet * YARDS))
print("Miles: %.2f" % (feet * MILES)) """

""" # Area circle and volume sphere

# Read the radius from user
raggio = float(input("Inserisci il raggio: "))

# Compute area and volume
area = math.pi * (raggio ** raggio)
volume = (4 / 3) * math.pi * pow(raggio, 3)

# Display the results
print("Area del cerchio: %.2f" % area)
print("Volume della sfera: %.2f" % volume) """

""" # Heat Capacity

# Read the mass of water and the temperature change
mass_water = float(input("Inserisci la quantità d'acqua in ml: "))
temperature = float(input("Inserisci il cambio di temperatura desiderato in gradi Celsius: "))

# Define constants for heat capacity and electricity costs
HEAT_CAPACITY = 4.186
ELEC_COST = 8.9 # cents
J_TO_KWH = 2.777e-7

# Compute energy needed
energy_needed = mass_water * temperature * HEAT_CAPACITY

# Conversion in kwh
kwh = energy_needed * J_TO_KWH

# Compute the cost of energy
cost = kwh * ELEC_COST

# Display the results
print("Energia necessaria: %d Joule" % energy_needed)
print("Costo riscaldamento acqua: %.2f cents" % cost) """

""" # Volume of a Cylinder

# Read radius and height from user
radius = float(input("Inserire il raggio: "))
height = float(input("Inserire l'altezza: "))

# Compute base area and volume
area = math.pi * pow(radius, 2)
volume = area * height

# Display the result
print("Volume cilindro: %.1f" % volume) """

""" # Free fall

# Constant of acceleration due to gravity
GRAVITY = 9.8

# Read the height from witch the object is dropped from user
height = float(input("Inserire l'altezza in metri: "))

# Compute final speed
velocita_finale = math.sqrt(2 * height * GRAVITY)

# Display the result
print("Velocità al momento dell'impatto: %.2f m/s" % velocita_finale) """

""" # Area of a Triangle (3 sides)

# Read the sides from user
s1, s2, s3 = input("Inserisci i 3 lati: ").split()
s1,s2,s3 = [float(s1), float(s2), float(s3)]

# Compute the area
s = (s1 + s2 + s3) / 2
area = math.sqrt(s * (s - s1) * (s - s2) * (s - s3))

# Display the result
print("Area del triangolo: %.2f" % area) """

""" # Area of a regular polygon

# Read the length of a side and the number of the sides
length_sides, num_sides = input("Inserisci la lunghezza dei lati ed il loro numero \nseparati da uno spazio: ").split()
length_sides, num_sides = [float(length_sides), int(num_sides)]

# Compute the area of the polygon
area = (num_sides * (length_sides ** 2)) / (4 * math.tan(math.pi / num_sides))

# Display the result
print("Area del poligono: %.2f" % area) """

""" # Units of Time

days, hours, minutes, seconds = input("Inserisci il tempo: ").split()
days, hours, minutes, seconds = [int(days), int(hours), int(minutes), int(seconds)]
days = days * 24
hours = ((hours + days) * 60)
minutes = ((minutes + hours) * 60)
seconds = seconds + minutes
print("Tempo in secondi:", seconds) """

""" # Units of time (again)

# Convert seconds in days, hours and minutes
DAY = 86400
HOURS = 3600
MINUTES = 60

# Read time in seconds from user
time = int(input("Inserire il tempo in secondi: "))

# Compute in form D:HH:MM:SS
day = 0; hours = 0; minutes = 0
while time > 0:
    if time > DAY:
        day = time / DAY
        time = time % DAY
    elif time > HOURS:
        hours = time / HOURS
        time = time % HOURS
    elif time > MINUTES:
        minutes = time / MINUTES
        time = time % MINUTES
    else:
        break

# Display the result
print("Tempo: %d:%02d:%02d:%02d" % (day, hours, minutes, time)) """

""" # Current Time
from time import asctime
time = asctime()
print(time) """

""" # When is Easter

# Read the year from user
anno = int(input("Per conoscere la data in cui cade la Santa Pasqua,\ndevi prima digitare l'anno: "))

# Gregorian algorithm as function
def easter(year: int) -> str:
    a = year % 19
    b = year // 100
    c = year % 100
    d = b // 4
    e = b % 4
    f = (b + 8) // 25
    g = (b - f + 1) // 3
    h = (19 * a + b - d - g + 15) % 30
    i = c // 4
    k = c % 4
    l = (32 + 2 * e + 2 * i - h - k) % 7
    m = (a + 11 * h + 22 * l) // 451
    month = (h + l - 7 * m + 114) // 31
    day = 1 + ((h + l - 7 * m + 114) % 31)
    print("Data Santa Pasqua per l'anno %d: %d/%d/%d" % (year, day, month, year))

# Display the result
easter(anno) """

""" # Body Mass Index

# Read height ed weight from user
height, weight = input("Inserisci l'altezza in metri ed il peso in kg: ").split()

# Convert the variables from string to float
height, weight = [float(height), float(weight)]

# Compute the BMI
bmi = weight / (height * height)

# Display the result
print("Il tuo indice di massa corperea è: %.2f" % bmi) """

""" # Wind Chill

# Constant required by the formula
WC_OFFSET = 13.12
WC_FACTOR1 = 0.6215
WC_FACTOR2 = 11.37
WC_FACTOR3 = 0.3965
WC_EXPONENT = 0.16

# Read air temperature and wind speed
tem = float(input("Inserisci la temperatura in gradi celsius: "))
wind = float(input("Inserisci la velocità del vento in km/h: "))

# Compute Wind Chill
wci = WC_OFFSET + \
      WC_FACTOR1 * tem - \
      WC_FACTOR2 * wind ** WC_EXPONENT + \
      WC_FACTOR3 * tem * wind ** WC_EXPONENT

# Diplay the result rounded to the closest integer
print("Indice vento gelido:", round(wci)) """

""" # Celsius to Fahrenheit and Kelvin

# Conversion factor constants
FAH = 32
KEL = 273.15

# Read the temperature in degrees Celsius
degrees = float(input("Qual è la temperatura in gradi centigradi? "))

# Convert the temperature in Fahrenheit and Kelvin
fahren = degrees + FAH
kelvin = degrees + KEL

# Display the results
print("Temperatura in gradi Fahrenheit", fahren)
print("Temperatura in gradi Kelvin", kelvin) """

""" # Units of Pressure

# Conversion constants
POUNDS_PER_SQUARE = 0.145038
MM_OF_MERCURY = 7.50062
ATMOSPHERE = 0.00986923

# Read the pressure in kilopascals
pascal = float(input("Inserisci la pressione in kilopascals: "))

# Compute the equivalent pressure
pounds_square = pascal * POUNDS_PER_SQUARE
mm_mercury = pascal * MM_OF_MERCURY
atmos = pascal * ATMOSPHERE

# Display the results
print("La pressione in libbre per pollice quadrato è: %.2f" % pounds_square)
print("La pressione in millimetri di mercurio è: %.2f" % mm_mercury)
print("La pressione in atmosfere è: %.2f" % atmos) """

""" # Sum of the Digits in an Integer

num = input("Inserisci un numero di 4 cifre: ")

a, b, c, d = [num[0], num[1], num[2], num[3]]
a, b, c, d = [int(a), int(b), int(c), int(d)]
print(a, "+", b, "+", c, "+", d, "=", a+b+c+d) """

""" # Sort 3 Integers

a = int(input("Inserisci il primo numero: "))
b = int(input("Inserisci il secondo numero: "))
c = int(input("Inserisci il terzo numero: "))
minimum = min(a, b, c)
maximum = max(a, b, c)
medium = a + b + c - minimum - maximum
print(minimum)
print(medium)
print(maximum) """

""" # Day Old Bread

COST = 3.49
DISCOUNT_PERC = 0.60

bread = int(input("Quanto pane vuoi comprare? "))

price = bread * COST
discount = bread * COST * DISCOUNT_PERC
total = price - discount

print("Prezzo del pane:          %5.2f" % price)
print("Sconto effettuato:        %5.2f" % discount)
print("Importo totale da pagare: %5.2f" % total) """
