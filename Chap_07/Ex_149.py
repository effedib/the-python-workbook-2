# Display the Head of a File
# Display the head (first 10 lines) of a file whose name is provided as a command line argument.

import sys

NUM_LINES = 10

# Verify that exactly one command line argument (in addition to the .py file) was supplied
if len(sys.argv) != 2:
    print('A file name must be provided as a command line argument')
    quit()

try:
    # Open the file for reading
    fin = open(sys.argv[1], 'r', encoding='utf-8')

    # Read the first line from the file
    line = fin.readline()

    # Keep looping until we have either read and displayed 10 lines or we have reached the end of the file
    i = 1
    while i <= NUM_LINES and line != '':
        # Remove the trailing newline character and count the line
        line = line.rstrip()

        print('{}: {}'.format((i), line))

        i += 1

        line = fin.readline()

    fin.close()

except FileNotFoundError:
    print('File not found, try again')
    quit()

except IOError:
    print('An error occurred while accessing the file.')
    quit()
