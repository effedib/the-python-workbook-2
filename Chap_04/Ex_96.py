def isInteger(string: str) -> bool:
    digits = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
    if string == "":
    
        return False
    
    elif string[0] == '+' or string[0] == '-':
        for i in string[1:]:
            if not i in digits:
            
                return False
            
    else:
        for i in string:
            if not i in digits:
                
                return False
        
    return True

def main():
    integ = input("Enter a string to verify if it's a string: ").strip()
    verify = isInteger(integ)
    if verify is True:
        print("The string is an Integer")
    else:
        print("The string is not an Integer")

if __name__ == "__main__":
    main()