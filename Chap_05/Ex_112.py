# Remove Outliers

# This function takes a list of values and an non-negative integer n as its parameter and returns a new copy of the list
# with the n largest and smallest elements removed, than the program reads a list of integers from the user and
# demonstrates the function

def remove_outliers(list_int: list, n: int) -> list:
    new_list = sorted(list_int)

    for i in range(n):
        new_list.pop()
        new_list.pop(0)

    return new_list


def main():
    # Read the first int from the user
    num = int(input("Enter an integer (0 to quit): "))

    # Create an empty list
    list_int = []

    # Loop to append integers into the list until 0 is entered
    while num != 0:
        list_int.append(num)
        num = int(input("Enter another integer (0 to quit): "))

    # Control if the lenght of the list is less than 4 values
    if len(list_int) < 4:
        print("Not enough values have been entered")
    else:
        print("This is the list with the two largest and smallest outliers removed: {}"\
              .format(remove_outliers(list_int, 2)))
        print("This is the original list: {}".format(list_int))


if __name__ == "__main__":
    main()
