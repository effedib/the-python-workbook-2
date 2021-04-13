# Reverse Lookup

# This function finds all of the keys in a dict that map to a specific value and returns a (possibly empty) list of
# keys from the dict.

def reverseLookup(dictionary: dict, value) -> list:

    keys_map = []
    for key in dictionary:
        if dictionary[key] == value:
            keys_map.append(key)

    return keys_map


def main():

    dic = {
        "Activision":   "COD",
        "Tencent":      "COD",
        "Ubisoft":      "Assassin's Creed",
        "Epic Games":   "Fortnite"
    }

    game = input('Enter a game to find the developer company (blank to quit): ')
    dev = reverseLookup(dic, game)

    while game != "":
        if dev:
            print('\nThe developer company of {} is/are: {}'.format(game, dev))
        else:
            print('\nUnfortunately I don\'t know which is the developer company for this game!')

        game = input('\nEnter a game to find the developer company (blank to quit): ')
        dev = reverseLookup(dic, game)


if __name__ == "__main__":
    main()
