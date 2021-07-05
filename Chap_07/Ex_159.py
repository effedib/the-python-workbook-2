# Two Word Random Password
# Generate a password from two randomly selected words (capitalize both words).
# The password must be length between 8 and 10 chars.

import random


# @file is a file where the function selects two words randomly
# @return the new password capitalized
def random_password(file: str) -> str:
    try:
        fin = open(file, 'r', encoding='utf-8')

    except:
        print('A problem was encountered while generating the password')
        print('Quitting...')
        quit()

    # Create a list to store the words with length between 3 and 7 chars
    words = []
    for line in fin:
        if 7 >= len(line) >= 3:
            line = line.rstrip()
            words.append(line.capitalize())

    # close the file
    fin.close()

    # select randomly two words in words list until the length of password is between 8 and 10 chars.
    password = ''
    while not 10 >= len(password) >= 8:
        first_word = words[random.randint(0, len(words))]
        second_word = words[random.randint(0, len(words))]
        password = first_word+second_word

    return password


def main():
    print('New Password: {}'.format(random_password('word.txt')))


if __name__ == '__main__':
    main()
