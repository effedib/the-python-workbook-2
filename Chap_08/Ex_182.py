# Spelling with Element Symbols

# This function determines whether or not a word can be spelled using only element symbols.


# @param word is the word to check
# @param sym is the list of symbols to combine to create the word
# @param result is the string to return at the end, it was initialized as empty string
# @param index is the index to be increased to iterate the list "sym" calling the recursion
def combineElements(word: str, sym: list, result: str = "", index: int = 0) -> str:

    # base conditions, if word == result or if it's impossible to combine elements
    if result.replace(' - ', '').upper() == word.upper():

        return result

    elif index >= len(sym):

        return "Impossible to spell the word {} with element symbols".format(word)

    else:

        # check if every letter is in "sym" and add to "result"
        if word[index].capitalize() in sym:

            if result == "":
                result += word[index].capitalize()

            else:
                result += " - " + word[index].capitalize()

            index += 1

            return combineElements(word, sym, result, index)

        # check if the double letter is a symbol and add to "result"
        elif index < (len(sym) - 2) and (word[index].capitalize() + word[index + 1]) in sym:

            if result == "":
                result += word[index].capitalize() + word[index + 1]

            else:
                result += " - " + word[index].capitalize() + word[index + 1]

            index += 2

            return combineElements(word, sym, result, index)

        else:

            return "Impossible to spell the word {} with element symbols".format(word)


def main():
    file = open('elements.txt')
    symbols = []

    for element in file:
        # Replace to delete the escape character but I don't need this index in the list, than I ignore it
        # line = line.replace("\n", "")
        element = element.split(",")
        symbols.append(element[1])
    file.close()

    word_to_check = input("Enter the word to check with element symbols: ")
    print(combineElements(word_to_check, symbols))


if __name__ == "__main__":
    main()
