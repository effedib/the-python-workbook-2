# Names that Reached Number One
# Read every file in the data set (names used from 1900 to 2012) and output two lists containing the most popular
# names for boys and girls. Neither of your lists should include any repeated values.

import os


folder = os.getcwd()+"\BabyNames"
boys = []
girls = []
for file in os.listdir(folder):
    path = os.path.join(folder, file)
    fin = open(path, 'r', encoding='utf-8')
    line = fin.readline()
    line = line.split()
    name = line[0]
    if 'Boys' in file:
        if name not in boys:
            boys.append(name)
    else:
        if name not in girls:
            girls.append(name)

print('Boys list:')
for i in range(len(boys)):
    print(boys[i])

print('\nGirls list:')
for i in range(len(girls)):
    print(girls[i])