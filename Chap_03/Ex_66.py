# No More Pennies

# Read prices from the user until a blank line is entered, display the total cost of all
# followed by the amount due if the customer pays with cash. The amount due should be rounded to the nearest nickel

PENNIES_PER_NICKEL = 5
NICKEL = 0.05

amount = input("Enter the amount (blank to quit): ")

tot_amount = 0
while amount != "":
    tot_amount += float(amount)

    amount = input("Enter the amount (blank to quit): ")

print("The exact amount payable is {:.2f}".format(tot_amount))

round_indicator = tot_amount * 100 % PENNIES_PER_NICKEL

if round_indicator < PENNIES_PER_NICKEL / 2:
    remainder = tot_amount - round_indicator / 100
else:
    remainder = tot_amount + NICKEL - round_indicator / 100

print("The cash amount payable is {:.2f}".format(remainder))
