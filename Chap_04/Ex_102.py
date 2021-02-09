# Check a Password

# This function determines whether or not a password is good.
# Check:
# At least 8 characters long
# At least 1 uppercase letter
# At least 1 lowercase letter
# At least 1 number
# @param the password to check

def checkPassword(password: str) -> bool:
    upper, lower, digit = (False, False, False)

    if len(password) >= 8:
        for c in password:
            if c.isupper():
                upper = True
            elif c.islower():
                lower = True
            elif c.isdigit():
                digit = True
    
    if upper and lower and digit:
        
        return True
    else:
        
        return False

def main():
    pwd = input("Enter the password: ")
    if checkPassword(pwd):
        print("This is a good password!")
    else:
        print("Password not safe!")

if __name__ == "__main__":
    main()
