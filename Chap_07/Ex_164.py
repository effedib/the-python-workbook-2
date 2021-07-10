# Gender Neutral Names
# Display all of the baby names that were used for both boys and girls in a year specified by the user.

import os


# @year_name is the birth year date to find in the name of the file
# @sex is type of file to check in that year (Boys or Girls)
# @folder = the folder within to search the files
# @return a list containing the names or a dict with values the n° of usage
def readNames(year_name: int, sex: str = 'Boys', folder: str = os.getcwd() + "\BabyNames",
              use_dict: bool = True) -> list or dict:

    # create the name of the file to find
    file = str(year_name) + '_' + sex + 'Names.txt'

    # join folder+file to create an absolute path
    path = os.path.join(folder, file)

    fin = open(path, 'r', encoding='utf-8')

    # read and split the file to create a list
    line = fin.read().split()

    # close the file before to exit the function
    fin.close()

    # if use_dict == False
    if not use_dict:
        # delete the 'non names' elements, all positioned in an odd index
        for name in line[1: (len(line) + 1): 2]:
            del line[line.index(name)]

        # return a list containing only the names
        return line

    else:

        dictNames = dict()
        for index, element in enumerate(line[::2]):
            # find the element after the name using (list.index+1) and re-cast to int
            dictNames[element] = int(line[line.index(element) + 1])

        # return a dict with values the n° of usage
        return dictNames


def main():

    # the range of years that the user can digit
    FIRST_YEAR = 1900
    LAST_YEAR = 2012

    # create a list for neutral names
    neutral = []

    # try to read the input from user like int or display an error message
    try:
        year = int(input('Enter the year to check if there were gender neutral names: '))

    except ValueError:
        print('You must enter a year!')
        print('Quitting...')
        quit()

    if LAST_YEAR >= year >= FIRST_YEAR:

        line_boys = readNames(year, use_dict=False)
        line_girls = readNames(year, sex='Girls', use_dict=False)

        # if the name is mentioned in both files append to neutral list
        for name in line_boys:
            if name in line_girls:
                neutral.append(name)

        # if neutral is not empty print...
        if neutral:
            print('Gender neutral names for year {}:'.format(year))
            for gender in neutral:
                print(gender)

        else:
            print('There aren\'t gender neutral names for year {}'.format(year))
    else:
        print('The year have to be entered between 1900 and 2012!')


if __name__ == '__main__':
    main()
