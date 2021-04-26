# String Edit Distance

# Write a recursive function to compute the edit distance between two string.


def compute_edit_distance(string1: str, string2: str, cost: int=0) -> int:

    if len(string1) == 0:

        return len(string2)

    elif len(string2) == 0:

        return len(string1)

    else:

        if string1[len(string1)-1] != string2[len(string2)-1]:
            cost = 1
        d1 = compute_edit_distance(string1[:len(string1)-1], string2) + 1
        d2 = compute_edit_distance(string1, string2[:len(string2)-1]) + 1
        d3 = compute_edit_distance(string1[:len(string1)-1], string2[:len(string2)-1]) + cost

        return min(d1, d2, d3)


def main():
    word1 = input('Enter the first string: ')
    word2 = input('Enter the second string: ')
    print("The edit distance between '{}' and '{}' is: {}".format(word1, word2, compute_edit_distance(word1, word2)))


if __name__ == "__main__":
    main()
