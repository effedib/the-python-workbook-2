# Days in a Month

from Ex_91 import isLeap

def dayin1month(month: int, year: int) -> int:

    if month in [4, 6, 9, 11]:

        return 30

    elif month == 2 and isLeap(year) is False:

        return 28
    
    elif month == 2 and isLeap(year) is True:

        return 29
    
    else:

        return 31

def main():
    month = int(input("Enter the month to control: "))
    year  = int(input("Enter the year to control: "))
    print("The month {} in the year {} has {} days".format(month, year, dayin1month(month, year)))

if __name__ == "__main__":
    main()