# Does a String Represent an Integer?

def isInteger(string: str) -> bool:
    string = string.strip()
    string = string.replace(' ', '')
    if string == "":
    
        return False
    
    elif string[0] == '+' or string[0] == '-':
        for i in string[1:]:
            if not i.isdigit():
            
                return False
            
    else:
        for i in string:
            if not i.isdigit():
                
                return False
        
    return True

def main():
    integ = input("Enter a string to verify if it's a string: ")
    verify = isInteger(integ)
    if verify is True:
        print("The string is an Integer")
    else:
        print("The string is not an Integer")

if __name__ == "__main__":
    main()