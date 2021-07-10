# Most Births in a given Time Period
# Determine which name were used most often within a time period decided by the user (always in a range 1900 and 2012).

from Chap_07.Ex_164 import readNames


# @f_year and l_year are the range of years within to find the names to store in "total_used"
# @sex is type of file to check (Boys or Girls)
# @return a dict of most used names between f_year and l_year
def MostUsedNames(f_year: int = 1900, l_year: int = 2012, sex: str = 'Boys') -> dict:

    total_used = dict()
    for year in range(f_year, l_year + 1):
        if total_used == {}:
            total_used = readNames(year, sex=sex)
        else:
            most_used = readNames(year, sex=sex)
            for key, value in most_used.items():
                if key not in total_used:
                    total_used[key] = value
                else:
                    total_used[key] += value

    return total_used


# @total_names is a dict of names with int values to sort and print
# @num_display is the number of items to display
def printNames(total_names: dict, num_display: int = 10):

    total_names = sorted(total_names.items(), key=lambda x: x[1], reverse=True)

    for index, element in enumerate(total_names):
        if index < num_display:
            print('{}: {}'.format(element[0], element[1]))
        else:
            break


def main():

    # the range of years that the user can digit
    FIRST_YEAR = 1900
    LAST_YEAR = 2012

    # try to read the input from user like int or display an error message
    try:
        start_year = int(input('Enter the start year to determine which names were used most often: '))
        last_year = int(input('Enter the last year: '))

    except ValueError:
        print('You must enter a year!')
        print('Quitting...')
        quit()

    if (not LAST_YEAR >= start_year >= FIRST_YEAR) and (not LAST_YEAR >= last_year >= FIRST_YEAR):
        print('The years have to be entered between 1900 and 2012!')

    else:

        total_boys = MostUsedNames(start_year, last_year)
        total_girls = MostUsedNames(start_year, last_year, sex='Girls')

        print('\nHere are the 10 most used boys names between years {} and {}:'.format(start_year, last_year))
        printNames(total_boys)

        print('\nHere are the 10 most used girls names between years {} and {}:'.format(start_year, last_year))
        printNames(total_girls)


if __name__ == '__main__':
    main()
