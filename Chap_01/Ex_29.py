# Wind Chill

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
print("Indice vento gelido:", round(wci))
