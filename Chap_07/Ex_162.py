# A Book with No E...

# import a function to order the dict without changing the type dict
from collections import OrderedDict


def usageLetters(file: str) -> tuple:
    alphabet = {
        'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0,
        'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0,
        'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0,
        'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0,
        'Y': 0, 'Z': 0
    }

    try:
        fin = open(file, 'r', encoding='utf-8')
        line = fin.read()

    except:
        print('Maybe you can\'t access the file')
        print('Quitting...')
        quit()

    try:

        # count the letter recurrence
        for letter in line:
            if letter.upper() in alphabet:
                alphabet[letter.upper()] += 1

        # Close the file
        fin.close()

        # sum the values to calculate the proportion
        total = sum(alphabet.values())

        # calculate the letter with less usage
        minimum_target = min(alphabet.values())

        # transform the number of time a letter is used in a tuple containg that value and # the proportion
        for key in alphabet:
            alphabet[key] = (alphabet[key], round(((alphabet[key] / total) * 100), 2))

        # create a list containing the letters with minimum values
        minimum_values = []

        # determine whitch letter is less used
        for key in alphabet:
            if alphabet[key][0] == minimum_target:
                minimum_values.append((key, alphabet[key]))

        # order the dict
        alphabet = OrderedDict(sorted(alphabet.items(), key=lambda x: x[1], reverse=True))

        # return a tuple containing the dict and a list containg the number of usage
        return alphabet, minimum_values

    except:
        print('An error occurred while processing the file')
        print('Quitting...')
        quit()


def main():
    use_dict, min_lst = usageLetters('sherlock.txt')

    for l in use_dict:
        print('{}: {:.2f}%'.format(l, use_dict[l][1]))

    print()
    print('Letter(s) with less or null usage:')

    for minimum in min_lst:
        print(minimum)


if __name__ == '__main__':
    main()
