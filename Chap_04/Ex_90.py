# The Twelve Days of Christmas

# This function displays the complete lyrics for The Twelve Days of Christmas song.

def TwelveDaysChristmas(num: int) -> str:
    from Ex_89 import OrdinalNumber
    
    gifts = {
         0: 'A partridge in a pear tree',
         1: 'And a partridge in a pear tree',
         2: 'Two turtle doves',
         3: 'Three french hens',
         4: 'Four calling (colly) birds',
         5: 'Five golden (gold) rings',
         6: 'Six geese a-laying',
         7: 'Seven swans a-swimming',
         8: 'Eight maids a-milking',
         9: 'Nine ladies dancing',
        10: 'Ten lords a-leaping',
        11: 'Eleven pipers piping',
        12: 'Twelve drummers drumming'
    }

    print("\nOn the {} day of Christmas\nmy true love sent to me:".format(OrdinalNumber(num)))
    if num == 1:
        print(gifts[0])
    else:
        for i in reversed(range(1, num+1)):
            print(gifts[i])

def main():
    for i in range(1, 13):
        TwelveDaysChristmas(i)

if __name__ == "__main__":
    main()