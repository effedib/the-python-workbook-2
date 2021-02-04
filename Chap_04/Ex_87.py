# Shipping Calculator

# This function takes the number of items in an orger for an online retailer and returns the shipping charge

def ShippingCharge(items: int) -> float:
    FIRST_ORDER  = 10.95
    SUBSEQ_ORDER =  2.95

    ship_charge = FIRST_ORDER + (SUBSEQ_ORDER * (items - 1))

    return ship_charge

def main():
    order = int(input("How many items are included in your order? "))
    shipping_charge = ShippingCharge(order)
    print("Shipping Charge: {:.2f}".format(shipping_charge))

if __name__ == "__main__":
    main()