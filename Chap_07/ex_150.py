import sys
import time

if len(sys.argv) != 2:
    print('A file name must be provided as a command line argument')
    quit()

begin = time.time()

inf = open(sys.argv[1], 'r', encoding='utf-8')

lines = []

for line in inf:
    lines.append(line)
    if len(lines) > 10:
        lines.pop(0)

inf.close()

for line in lines:
    print(line)
end = time.time()
print('\nTime2: {:.2f}\n'.format(end - begin))
