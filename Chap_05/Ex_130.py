# Unary and Binary Operators

def unary(tokens: list) -> list:
    operators = ['*', '/', '^', '+', '-', '(']

    for i, s in enumerate(tokens):
        if s in ['+', '-'] and (i == 0 or tokens[i-1] in operators):
            tokens[i] = 'u' + s

    return tokens


def main():
    print(unary(['-', '52', '+', '+', '3', '-', '-', '86', '*', '936', '/']))


if __name__ == "__main__":
    main()
