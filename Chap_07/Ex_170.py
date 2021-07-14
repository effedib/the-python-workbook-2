# Missing Comments

import os


folder = os.getcwd()
missing_lst = []

for file in os.listdir(folder):

    path = os.path.join(folder, file)
    if file != 'Ex_170.py' and os.path.isfile(path) and file.endswith('.py'):
        fin = open(path, 'r', encoding='utf-8')

        txt_line = fin.readline()
        previous = ''
        line = 1

        while txt_line != '':
            if txt_line.startswith('def ') and not previous.startswith('#'):
                bracket_pos = txt_line.index('(')
                missing_lst.append((file, line, txt_line[4:bracket_pos]))
            previous = txt_line
            txt_line = fin.readline()
            line += 1

        fin.close()

for file_miss, row, function in missing_lst:
    print("Comments missing in file: {}, line: '{}', function: '{}'".format(file_miss, row, function))
