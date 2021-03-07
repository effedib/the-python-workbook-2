# Tokenizing a String

# Tokenizing is the process of converting a string into a list of substrings, known as tokens.

def tokenbystring(string: str) -> list:
    string = string.replace(' ', '')
    tokens = []
    dgt = ''
    for s in string:
        if s in ['*', '/', '^', '+', '-', '(', ')']:
            if dgt != '':
                tokens.append(dgt)
            dgt = ''
            tokens.append(s)
        elif 0 <= int(s) <= 9:
            dgt += s
            if s == string[len(string)-1]:
                tokens.append(dgt)

    return tokens


def main():
    # exp = input("Enter a mathematical expressione: ")
    exp = '52 + 3 - 86 * (936 / 2)'
    print('The tokens are: {}'.format(tokenbystring(exp)))


if __name__ == "__main__":
    main()
