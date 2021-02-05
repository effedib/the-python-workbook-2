# Convert an Integer to Its Ordinal Number

# This function takes an integer as its only parameter and returns a string containing the appropriate English ordinal number.

def OrdinalNumber(num: int) -> str:
    ordinals = {
         1: 'First',
         2: 'Second',
         3: 'Third',
         4: 'Fourth',
         5: 'Fifth',
         6: 'Sixth',
         7: 'Seventh',
         8: 'Eighth',
         9: 'Ninth',
        10: 'Tenth',
        11: 'Eleventh',
        12: 'Twelfth'
    }

    return ordinals[num]

def main():
    for i in range(1, 13):
        print("{}: {}".format(i, OrdinalNumber(i)))

if __name__ == "__main__":
    main()