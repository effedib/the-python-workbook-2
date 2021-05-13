# Run-Length Decoding
# This function decompresses a run-length encoded list, taking only  a compressed list as its only parameter.

# @lst is the run-length encoded list to decompress
# @return the new decompressed list
def decompressedList(lst: list) -> list or str:

    if type(lst) != list:

        # Control if the taken parameter is a list
        return "You can decode only lists!!!!"

    # New list to return
    decomp_lst = []

    # Base condition if the length of the list is >1, append n times the first element of the list like the second
    # element of the list
    if len(lst) > 1:
        for i in range(lst[1]):
            decomp_lst.append(lst[0])

        # calls the function recursively to decompress the remaining list with the same logic and returning the new list
        return decomp_lst + decompressedList(lst[2:])

    else:

        # if the length is less than 1, return the new list + the empty old list
        return decomp_lst + lst


def main():
    list_prova = ['A', 12, 'B', 4, 'A', 6, 'B', 1, 'C']
    list_prova2 = [7, 12]
    list_prova3 = (7, 12)
    print(decompressedList(list_prova))
    print(decompressedList(list_prova2))
    print(decompressedList(list_prova3))


if __name__ == "__main__":
    main()
