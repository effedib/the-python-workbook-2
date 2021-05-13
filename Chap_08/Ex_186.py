# Run-Length Encoding
# This recursive function implements the run-length compression technique and compresses a string taken as its only
# parameter.

# @lst is the string to compress
# @return the new compressed list
def compressList(string: str) -> list or str:

    if type(string) != str:

        # Control if the taken parameter is a string
        return "You can decode only strings!!!!"

    # The new encoded list
    lst = []

    # Base condition
    if string != "":

        # loop to check the string and update lst
        for i, c in enumerate(string):
            if not lst:
                lst = [c, 1]
            else:
                if string[i] == lst[0]:
                    lst[1] += 1
                else:

                    # if the remaining list is different, call the function recursively
                    return lst + compressList(string[i:])

        return lst

    else:

        return lst


def main():
    # list1 = ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'A', 'A', 'A', 'B', 'C']
    string1 = input("Enter a string to encode: ")
    print(compressList(string1))


if __name__ == "__main__":
    main()
