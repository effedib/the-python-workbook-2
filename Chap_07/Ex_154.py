# Letter frequencies
# Determinate the frequency of all of the letters in a file ignoring spaces, punctuation marks and digits.
# The program is case insensitive


import string
import time
import sys

if len(sys.argv) < 2:
    print('A file name must be provided as a command line argument')
    quit()

now = time.time()
try:
    fin = open(sys.argv[1], 'r', encoding='utf-8')

except:
    print('Impossible to open the file! I\'m opening the file element.txt')
    fin = open('elements.txt', 'r', encoding='utf-8')

line = fin.read()

now = time.time() - now
print('\nTime elapsed to read the file: {:.2f}'.format(now))

counter = dict()

for l in line:
    if l not in string.punctuation and l not in string.whitespace and not l.isdigit():
        if l not in counter:
            counter[l.lower()] = 1
        else:
            counter[l.lower()] += 1

now = time.time() - now
print('\nTime elapsed to count the letters: {:.2f}'.format(now))

for k in counter:
    print("{}: {}".format(k, counter[k]))

now = time.time() - now
print('\nTime elapsed to print the results: {:.2f}'.format(now))

fin.close()
