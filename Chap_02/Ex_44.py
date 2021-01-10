# Faces on Money

# Read an amount from user to find the individual (if any) that appears on that banknote

WASHINGTON = 1
JEFFERSON = 2
LINCOLN = 5
HAMILTON = 10
JACKSON = 20
GRANT = 50
FRANKLIN = 100

# Read the amount from user
banknote = float(input('Enter the banknote: '))

# Find the individual
if banknote == WASHINGTON:
    individual = 'George Washington'
elif banknote == JEFFERSON:
    individual = 'Thomas Gefferson'
elif banknote == LINCOLN:
    individual = 'Abraham Lincoln'
elif banknote == HAMILTON:
    individual = 'Alexander Hamilton'
elif banknote == JACKSON:
    individual = 'Andrew Jackson'
elif banknote == GRANT:
    individual = 'Ulysses S. Grant'
elif banknote == FRANKLIN:
    individual = 'Benjamin Franklin'
else:
    individual = ''

if individual == '':
    print('The selected banknote doesn\'t exists!')
else:
    print('The face that appears on the banknote is: \"{:s}\"'.format(individual))