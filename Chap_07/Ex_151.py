# Concatenate Multiples Files

import sys

if len(sys.argv) < 2:
  print('A file name must be provided as a command line argument')
  quit()

try:
  
  for file in sys.argv[1:]: 
    fin = open(file, 'r', encoding='utf-8')

    print('START OF FILE: {}'.format(file))
    
    for line in fin:
      print(line, end='')

    print('END OF FILE: {}\n'.format(file))
    fin.close()

except FileNotFoundError:
  print('File {} not found, try again'.format(file))
  quit()

except IOError:
  print('An error occurred while accessing the file {}.'.format(file))
  quit()
