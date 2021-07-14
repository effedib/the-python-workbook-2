# Redacting Text in a File

def splitString(line: str) -> list:
    from re import split

    line_lst = split("[,.?!:; '0123456789\n]", line)

    clean = False
    while not clean:
        if "" in line_lst:
            line_lst.remove("")
        else:
            clean = True

    return line_lst


def redact(string: str, s_file: str) -> str:
    with open(s_file, 'r', encoding='utf-8') as sensitive_file:

        sensitives = set(sensitive_file.read().split())

        line = splitString(string)

        to_redact = []

        for sensitive_word in sensitives:
            if sensitive_word.lower() in string.lower():
                for word in line:
                    if word.lower() == sensitive_word.lower():
                        to_redact.append(word)

        for index in range(len(to_redact)):
            string = string.replace(to_redact[index], ('*' * len(to_redact[index])))

        return string


def main():
    f_input = input('Enter the file to redact: ')
    f_output = input('Enter the name of the new file to create: ')
    sensitive_file = input('Enter the name of the sensitive file: ')

    with open(f_input, 'r', encoding='utf-8') as fin, \
            open(f_output, 'w', encoding='utf-8') as fout:
        lines = fin.readline()

        while lines != '':
            new_string = redact(lines, sensitive_file)
            fout.write(new_string)
            lines = fin.readline()


if __name__ == '__main__':
    main()
