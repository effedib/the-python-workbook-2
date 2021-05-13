# Flatten a list
# This function implements a recursive flattening algorithm taking a list to flatten as only parameters and returning
# the flattened list.


def flattenList(nested_list: list) -> list:
    # Base condition if the list is empty
    if not nested_list:
        return []

    # if the first element of the list is a list, call the function recursively until the entire list is flatten
    elif type(nested_list[0]) is list:
        return flattenList(nested_list[0]) + flattenList(nested_list[1:])

    # if the first element is not a list only the remaining elements need to be flatten
    else:
        return [nested_list[0]] + flattenList(nested_list[1:])


def main():
    data = [1, [2, 3], [4, [5, [6, 7]]], [[[8], 9], [10]]]
    data2 = [[1, 2, 3], ['a', 'b', 'c'], [7], [8, 9, 'd']]
    data_empty = []
    print("{}\n{}\n{}".format(flattenList(data), flattenList(data2), flattenList(data_empty)))


if __name__ == "__main__":
    main()
