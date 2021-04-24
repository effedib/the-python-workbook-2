# Total the Values
# Display the sum of the values entered by the user using recursion.

def sumbyuser():
    num = input("Enter a number to sum the total (blank to quit): ")
    if num == '':
        return 0.0

    return float(num) + sumbyuser()


def main():
    print("The total of all numbers entered is: {}".format(sumbyuser()))


if __name__ == '__main__':
    main()
