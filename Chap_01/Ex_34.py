# Day Old Bread

COST = 3.49
DISCOUNT_PERC = 0.60

bread = int(input("Quanto pane vuoi comprare? "))

price = bread * COST
discount = bread * COST * DISCOUNT_PERC
total = price - discount

print("Prezzo del pane:          %5.2f" % price)
print("Sconto effettuato:        %5.2f" % discount)
print("Importo totale da pagare: %5.2f" % total)