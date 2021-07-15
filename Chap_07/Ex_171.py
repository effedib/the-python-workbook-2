# Consistent Line Lengths

LINE_LENGTH = 80
file = 'UPPER.txt'
f_out = 'prova_lunghezza.txt'

with open(file, 'r', encoding='utf-8') as fin, \
        open(f_out, 'w', encoding='utf-8') as fout:
    text = fin.readline()

    i = 0
    while text != '':
        text = text.rstrip().split()
        for letter in text:
            if (len(letter) + i) < LINE_LENGTH:
                fout.write(letter + ' ')
                i = i + len(letter) + 1
            else:
                fout.write('\n' + letter + ' ')
                i = len(letter) + 1
        text = fin.readline()
        if text == '\n':
            fout.write(text)
            text = fin.readline()

print('File created')
