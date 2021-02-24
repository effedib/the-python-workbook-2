# Negatives, Zeros and Positives

# Read integers until blank line is entered. Display all of the negatives, followed by the zeros and for the last
# the positives. Within each group the numbers sholud be displayed in the same order that they were entered.

# Read the first int from the user
num = input('Enter an integer (blank to quit): ')

# Create 3 lists for 3 groups
negatives = []
zeroes = []
positives = []

# loop the question untile blank is entered to fill the lists
while num != '':
    num = int(num)
    if num < 0:
        negatives.append(num)
    elif num == 0:
        zeroes.append(num)
    elif num > 0:
        positives.append(num)
    else:
        # Wrong choise case
        num = input("Wrong value, enter an integer! ")
        continue
    num = input('Enter an integer (blank to quit): ')

# Merge the lists into one unique list
list_int = [negatives, zeroes, positives]

# Display the results
for i in list_int:
    for c in i:
        print(c)

