# Unique Characters

# Determine which is the number of unique characters that composes a string.

unique = dict()

string = input('Enter a string to determine how many are its unique characters and to find them: ')

for c in string:
    if c not in unique:
        unique[c] = 1

num_char = sum(unique.values())

print("'{}' has {} unique characters\nand it/they is/are:".format(string.upper(), num_char))

for c in unique:
    print("'{}'".format(c), end=' ')

