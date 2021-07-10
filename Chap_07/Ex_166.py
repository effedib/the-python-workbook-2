# Distinct Names
# Read every file in the baby names data set, keep track of every distinct name used for boys and girls, display both
# lists without any repeated value.

from Chap_07.Ex_164 import readNames


# @first_year and last_year are the range of years within to find the names
# @return tuples of data set for boys and girls names
def distUsedNames(first_year: int = 1900, last_year: int = 2012) -> tuple:

    # I need a list with no repeated names, so I use sets because they are faster to update and store
    boys_set, girl_set = set(), set()

    for year in range(first_year, (last_year+1)):
        boys_set.update(readNames(year, use_dict=False)) # I want a list without the usage of names so use_dict=False

    for year in range(first_year, (last_year+1)):
        girl_set.update(readNames(year, sex='Girls', use_dict=False))

    # return a tuple because I need to print every single element of the collection
    return tuple(boys_set), tuple(girl_set)


def main():

    boys, girls = distUsedNames()

    print('\nList of names used from 1900 to 2012:\n')

    for i in range(max(len(boys), len(girls))):
        this_boy = boys[i] if i < len(boys) else ''
        this_girl = girls[i] if i < len(girls) else ''
        print('{:20}\t{}'.format(this_boy, this_girl))


if __name__ == '__main__':
    main()

