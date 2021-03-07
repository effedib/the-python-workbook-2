# Operator Precedence

# This function return an integer representing the precedence of a mathematical operator

def precedence(operator: chr) -> int:
    list_operators = {'+': 1, '-': 1, '*': 2, '/': 2, 'u+': 3, 'u-': 3, '^': 4}

    if (len(operator) > 1 and operator not in ['u+', 'u-']) or \
            operator not in list_operators:
        return -1

    else:

        return list_operators[operator]


def main():
    op = input("Enter a mathematical operator: ")
    prec_op = precedence(op)
    if prec_op > 0:
        print("This operator has the precedence = {:d}".format(prec_op))
    else:
        print("This isn't a mathematical operator!")


if __name__ == "__main__":
    main()
