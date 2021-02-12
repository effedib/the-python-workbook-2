# Magic Dates

# This function determines if a date is or not a magic date (day * month = two digit year)

from Ex_106 import dayin1month

def isMagicDate(day: int, month: int, year: int) -> bool:
    if day * month == year % 100:
        
        return True
    
    return False

def main():
    for year in range(1901, 2000):
        for month in range(1, 13):
            for day in range(1, dayin1month(month, year + 1)):
                if isMagicDate(day, month, year):
                    print('{}-{}-{}'.format(day, month, year), end = '  ')

if __name__ == "__main__":
    main()