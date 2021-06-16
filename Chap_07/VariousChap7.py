import sys

# Ensure that the program was started with one command line argument beyond the name of the .py file
if len(sys.argv) != 2:
    print('A file name must be provided as a command line argument')
    quit()

# Open the file listed immediately after the .py file on the command line
inf = open(sys.argv[1], 'r', encoding='utf-8')

total = 0

line = inf.readline()
while line != '':
    total += float(line)
    line = inf.readline()

inf.close()

print("The total of the values in {} is {}".format(sys.argv[1], total))

