# Sum a Collection of Numbers

total = 0
number = input("Enter the first number (blank to quit): ")

while number != '':

    try:
        total += float(number)
        print("Total updated: {}\n".format(total))

    except ValueError:
        print("The value entered is incorrect! You have to insert a number.\n")

    number = input("Enter the next number (blank to quit): ")

print("\nFinal sum of all numbers entered by the user: {}".format(total))
