# Roulette Payouts

# Simulate the spin of a roulette wheel, display the number generated
# and the bets that must be payed

from random import randrange

# Generate a number between 0 to 36
bet = randrange(0,38)

# Classify the red numbers
red = (1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36)

# Display the bets that must be payed
if bet == 37:
    print("The spin generated is 00...")
    print("Pay 00")
else:
    print("The spin generated is {}...".format(bet))
    print("Pay {}".format(bet))
    if bet != 0:
        if bet in red:
            print("Pay Red")
        else:
            print("Pay Black")
        if bet % 2 == 0:
            print("Pay Even")
        else:
            print("Pay Odd")
        if bet < 19:
            print("Pay 1 to 18")
        else:
            print("Pay 19 to 36")