# Element Sequences

# This program reads the name of an element from the user and uses a recursive function to find the longest
# sequence of elements that begins with that value


# @param element is the element entered by the user
# @param elem_list is the list of elements to check to create the sequence
def elementSequences(element: str, elem_lst: list) -> list:

    if element == "":
        return []

    best_seq = []

    last_letter = element[len(element) - 1].lower()

    for i in range(len(elem_lst)):
        first_letter = elem_lst[i][0].lower()
        if first_letter == last_letter:
            candidate = elementSequences(elem_lst[i], elem_lst[:i] + elem_lst[i+1:len(elem_lst)])
            if len(candidate) > len(best_seq):
                best_seq = candidate

    best_seq = [element] + best_seq
    if len(best_seq) > 1 and best_seq[0] == best_seq[1]:
        del best_seq[0]

    return best_seq


def main():
    file = open('elements.txt')
    elements_lst = []

    for ele in file:
        # Replace to delete the escape character
        ele = ele.replace("\n", "")
        ele = ele.split(",")
        elements_lst.append(ele[2])

    file.close()

    element_to_start = input("Enter the word to start the sequence of elements: ")
    print(elementSequences(element_to_start, elements_lst))


if __name__ == "__main__":
    main()
