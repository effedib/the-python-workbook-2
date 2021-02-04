# Taxi Fare

# This function takes the distance travelled by a taxi (in kilometers) and returns the total fare

def taxifare(km: float) -> float:
    BASE_FARE   = 4.00
    CONSUM_FARE = (0.25 / 140) * 1000

    fare = BASE_FARE + CONSUM_FARE * km

    return fare

def main():
    km   = float(input("Enter the distance in km: "))
    bill = taxifare(km)
    print("Your bill is: {:.2f}".format(bill))

if __name__ == "__main__":
    main()