# Words that Occur Most

def onlywordsFile(line: str) -> list:

    from re import split

    line = line.lower()

    line_lst = split('[,.?!:; \'0123456789\n]', line)

    clean = False
    while not clean:
        if "" in line_lst:
            line_lst.remove("")
        else:
            clean = True

    return line_lst


def main():
    file = input('Enter the name of the file: ')

    try:
        fin = open(file, 'r', encoding='utf-8')

    except:
        print('File not found! Quitting...')
        quit()

    counter = dict()
    line = fin.readline()

    while line != "":
        word_lst = onlywordsFile(line)
        for word in word_lst:
            if word in counter:
                counter[word] += 1
            else:
                counter[word] = 1
        line = fin.readline()

    fin.close()

    i = 0
    for k in sorted(counter.items(), key=lambda x: x[1], reverse=True):
        if i < 50:
            print("{}: {}".format(k[0], k[1]))
        i += 1


if __name__ == "__main__":
    main()
