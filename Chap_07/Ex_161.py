# What's that Element Again?
# From a file that contains chemical elements determine which element matches with the input received from user even if
# the input is the symbol, the name or the number of protons for an element.

# try to open the file and create a list with 1 element for each line
try:
    fin = open('elements.txt', 'r')
    line = fin.read()
    line = line.split()

except:
    print("The file doesn't exists or maybe you can't access this file!")
    print('Quitting....')
    quit()


# generate 3 lists for symbols, elements e n° of protons to split every line
protons, symbs, elements = [], [], []

for index, element in enumerate(line):
    line[index] = element.split(',')
    protons.append(int(line[index][0]))
    symbs.append(line[index][1])
    elements.append(line[index][2])

# read the input from user
f_input = input("Choose if you want enter the symbol of an element, the name of an element or the number of protons"
                "of an element (blank to exit): ").capitalize()

while f_input != '':

    try:
        # try if the input entered is the number of protons
        f_input = int(f_input)
        i = protons.index(f_input)
        print('The element with {} protons is: {} - {}'.format(protons[i], symbs[i], elements[i]))

    except:

        try:
            # try if the input entered is the symbol of the element
            i = symbs.index(f_input)
            print('The element with symbol {} is: {} with n° protons = {}'.format(symbs[i], elements[i], protons[i]))

        except:

            try:
                # try if the input entered is the name of the element
                i = elements.index(f_input)
                print('The symbol for the {} is: {} and the n° protons is {}'.format(elements[i], symbs[i], protons[i]))

            except:
                # User entered a wrong value
                print('No elements exists for this name!')

    # loop until the user enters a blank line
    f_input = input("\nChoose if you want enter the symbol of an element, the name of an element or the number of"
                " protons of an element (blank to exit): ").capitalize()

