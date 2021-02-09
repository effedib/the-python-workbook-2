# Random Good Password

# Using the solutions to Exercised 100 and 102, this function generates a random good password and displays it.

from Ex_102 import checkPassword
from Ex_100 import randomPassword

def passwordGenerator() -> str and int:

    password = randomPassword()
    count = 1
    while not checkPassword(password):
        password = randomPassword()
        count += 1

    return password, count

def main():
    pwd, attempts = passwordGenerator()
    print("This is your password after {:d} attempts: {:s}".format(attempts, pwd))

main()