# Reduce Measures

# This function takes a number of units and the unit of measure (cup, tablespoon, teaspoon) as its parameter and
# returns a string representing the measure using the largest possible units.

def reduceMeasure(volume: int, unit: str) -> str:

    TEASPOON    = 1
    TABLESPOON  = 3
    CUP         = 48

    unit = unit.lower()
    if unit == 'tablespoon':
        volume *= TABLESPOON
    elif unit == 'cup':
        volume *= CUP  

    cups        = 0
    tablespoons = 0
    teaspoons   = 0

    strcups, strtablespoons, strteaspoon = ('cups', 'tablespoons', 'teaspoons')
    cups = volume // CUP
    if cups > 0:
        tablespoons = (volume % CUP) // TABLESPOON
        if tablespoons > 0:
            teaspoons = (volume % CUP) % TABLESPOON
    else:
        tablespoons = volume // TABLESPOON
        if tablespoons > 0:
            teaspoons = volume % TABLESPOON
        else:
            teaspoons = volume

    if cups == 1:
        strcups = 'cup'
    if tablespoons == 1:
        strtablespoons = 'tablepoon'
    if teaspoons == 1:
        strteaspoon = 'teaspoon'
    
    return "{} {}, {} {}, {} {}".format(cups, strcups, tablespoons, strtablespoons, teaspoons, strteaspoon)

def main():
    print(reduceMeasure(915, 'Tablespoons'))

if __name__ == "__main__":
    main()