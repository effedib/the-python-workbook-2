# Only the Words

# This function returns a list of the words in a string with the punctuation marks at the edges of the words removed.
from typing import List


def onlywords(line: str) -> list:
    from re import split
    words: List[str] = split('[,.?!:; ]', line)
    for count, word in enumerate(words):
        if word == '':
            del words[count]

    return words


def main():
    string = input("Enter the text: ")
    # string = "Contraction include: don't, isn't, and wouldn't"
    print(onlywords(string))


if __name__ == "__main__":
    main()
