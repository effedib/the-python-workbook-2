# Random License Plate

# Old license = 3 letters followed by 3 digits
# New license = 4 digits followed by 3 letters
# Generate a random license

def plateGenerator() -> str:
    from random import randint

    plate = ''
    if randint(1, 2) == 1:
        for i in range(6):
            if i < 3:
                plate += chr(randint(65, 90))
            else:
                plate += chr(randint(48, 57))
    else:
        for i in range(7):
            if i < 4:
                plate += chr(randint(48, 57))
            else:
                plate += chr(randint(65, 90))
    
    return plate

def main():
    print("Here is your plate: {:s}".format(plateGenerator()))

main()