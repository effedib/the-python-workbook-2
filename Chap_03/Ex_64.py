# Discount Table

# Display a table showing the original price, the discount amount and the new price for purchases

orig_price = [4.95, 9.95, 14.95, 19.95, 24.95]
for price in orig_price:
    disc = price * 0.60
    new_price = price - disc
    print("Original price: {:5.2f} - Discount amount: {:5.2f} - New price: {:5.2f}".format(price, disc, new_price))