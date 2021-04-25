# The NATO Phonetic Alphabet

# This function reads a word from the user and displays its phonetic spelling.


def phonetic_word(word: str) -> str:

    table = {
        'A': 'Alpha', 'B': 'Bravo', 'C': 'Charlie', 'D': 'Delta', 'E': 'Echo',
        'F': 'Foxtrot', 'G': 'Golf', 'H': 'Hotel', 'I': 'India', 'J': 'Juliet',
        'K': 'Kilo', 'L': 'Lima', 'M': 'Mike', 'N': 'November', 'O': 'Oscar',
        'P': 'Papa', 'Q': 'Quebec', 'R': 'Romeo', 'S': 'Sierra', 'T': 'Tango',
        'U': 'Uniform', 'V': 'Victor', 'W': 'Whiskey', 'X': 'Xray', 'Y': 'Yankee', 'Z': 'Zulu'
    }

    # Base Case
    if word == '':

        return word

    new_word = word.upper()

    # if the character is an integer or space, ignore it
    if word[0] not in table:

        return '' + phonetic_word(new_word[1:])

    return table[new_word[0]] + ' ' + phonetic_word(new_word[1:])


def main():
    string = input("Enter a word to spell: ")
    print(phonetic_word(string))


if __name__ == '__main__':
    main()
