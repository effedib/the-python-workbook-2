# Possible Change

# Read both the dollar amount and the number of coins from user and display a message indicating whether or not the
# entered amount can be formed using the number of coins indicated.


def possibleChange(dollars, coins, index=0):
    coins_list = [0.25, 0.10, 0.05, 0.01]

    dollars = round(dollars, 2)

    if dollars == 0 and coins == 0:
        return True

    elif index >= len(coins_list):
        return False

    print("index '{:.2f}'\t{:.2f} dollars\t{:.2f} coins".format(coins_list[index], dollars, coins))

    if dollars == 0 or coins == 0:
        dollars += coins_list[index]
        coins += 1
        index += 1
        return possibleChange(dollars, coins, index)

    elif (dollars / coins) in coins_list:
        return True

    else:
        if dollars >= coins_list[index]:
            dollars -= coins_list[index]
            coins -= 1
        else:
            index += 1
        return possibleChange(dollars, coins, index)


def main():
    total = float(input('Enter the total amount: '))
    coin = int(input('How many coins do you want to use? '))
    for i in range(1, (coin+1)):
        print("{} coins:\t{}".format(coin, possibleChange(total, coin)))


if __name__ == "__main__":
    main()
