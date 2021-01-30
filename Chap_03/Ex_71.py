# Approzimate PI Greek

# Display 15 approximation of PI Greek
denominatore = 2
pi_greek = 3
for p in range(15):
    blocco_denominatore = (4 / (denominatore * (denominatore+1) * (denominatore+2)) - (4 / ((denominatore+2) * (denominatore+3) * (denominatore+4))))
    pi_greek += blocco_denominatore
    print(pi_greek)
    denominatore += 4