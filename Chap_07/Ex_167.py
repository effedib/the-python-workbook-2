# Spell Checker
# Read a file and display all of the words in it that are misspelled.

import sys


def misspelledWords(file: str) -> tuple:
    from re import split
    from time import time

    print('loading the controller file')
    start = time()
    with open('word.txt', 'r', encoding='utf-8') as controller:

        line = controller.readline()

        words_set = set()
        while line != '':
            line = line.lower()
            words_set.update(set(split("[,.?!:; 0123456789\n\"]", line)))
            line = controller.readline()

        words_set.remove('')
    end = time() - start
    print('File read in {:.2f} seconds'.format(end))

    print('\nloading the file to control')
    start = time()
    try:
        # Open the file listed immediately after the .py file on the command line
        with open(file, 'r', encoding='utf-8') as file_checked:

            line = file_checked.readline()

            words2check = set()
            while line != '':
                line = line.lower()
                words2check.update(set(split("[,.?!:; 0123456789\n\"]", line)))
                line = file_checked.readline()

            words2check.remove('')
        end = time() - start
        print('File read in {:.2f} seconds\n'.format(end))

    except IndexError:
        print('A file name must be provided as a command line argument')
        print('Quitting...')
        quit()

    except:
        print('An error occurred while accessing the file')
        print('Quitting...')
        quit()

    misspelled_words = set()

    for word in words2check:
        if word not in words_set:
            misspelled_words.add(word)

    return tuple(misspelled_words)


def main():

    misspelled_list = misspelledWords(sys.argv[1])

    for i, word in enumerate(misspelled_list):
        print(word)


if __name__ == '__main__':
    main()
