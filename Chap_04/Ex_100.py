# Random Password

# This function generates a random password with random length of between 7 and 10 characters

def randomPassword() -> str:
    from random import randint

    lenght = randint(7, 10)

    password = ""
    for i in range(lenght):
        password += chr(randint(33, 126))
    
    return password

def main():
    print("Password: {:s}".format(randomPassword()))

if __name__ == "__main__":
    main()