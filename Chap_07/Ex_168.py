# Repeated Words
# Detect repeated words in a text file

import sys
from Ex_155 import onlywordsFile


# @word_lst is a list of word to examine to determine if there are duplicates
# @return a string containing only duplicates or an empty string if there are no duplicates
def findDuplicate(word_lst: list) -> str:

    # store the dupl in a set because we want a collection of uniques elements
    duplicates_set = set()

    # index starts = 1 because the index 0 can't be a duplicate in this line
    for index, word in enumerate(word_lst[1:], 1):
        if word == word_lst[index - 1]:
            duplicates_set.add(word)

    return ', '.join(duplicates_set)


def main():

    try:

        fin = open(sys.argv[1], 'r', encoding='utf-8')

        file = fin.readline()
        # create a dict with keys = n° of the line to display
        duplicates = dict()
        # track the last element of the previous list to check if it's equal to the first element of the next list
        last = ''

        i = 1
        while file != '':
            # create a list of words from the line and find the duplicates (if there are)
            now = onlywordsFile(file)
            dupl = findDuplicate(now)

            # if the last element of the previous list it's equal to the first element of the next list = it's a dupl
            if len(now) > 0 and last == now[0]:
                duplicates[i] = last
            if dupl != '':
                if i in duplicates:
                    duplicates[i] += dupl
                else:
                    duplicates[i] = dupl

            # if now is a non empty string, last is equal to the last element of now
            if len(now) > 1: last = now[-1]
            elif len(now) == 1: last = now[0]
            else: last = ''

            file = fin.readline()
            i += 1

        fin.close()
        print(duplicates)

    except IndexError:
        print('A file name must be provided as a command line argument')
        print('Quitting...')
        quit()

    except:
        print('An error occurred while accessing the file')
        print('Quitting...')
        quit()


if __name__ == '__main__':
    main()
