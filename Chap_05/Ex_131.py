# Infix to Postfix

# Convert a mathematical expression from infix form to postfix form

from Chap_04.Ex_96 import isInteger
from Chap_04.Ex_97 import precedence
from Ex_129 import tokenbystring
from Ex_130 import unary


def infix2postfix(string_fun: str) -> list:
    unary_string = unary(tokenbystring(string_fun))
    operators = []
    postfix = []
    for t in unary_string:
        if isInteger(t):
            postfix.append(t)
        elif t in ['*', '/', '^', '+', '-', 'u+', 'u-']:
            while operators != [] and \
                  operators[len(operators)-1] != '(' and \
                  precedence(t) < precedence(operators[len(operators)-1]):
                postfix.append(operators.pop())
            operators.append(t)
        elif t == '(':
            operators.append(t)
        elif t == ')':
            while operators[len(operators)-1] != '(':
                postfix.append(operators.pop())
            operators.remove('(')
    while operators:
        postfix.append(operators.pop())

    return postfix


def main():
    string = input("Enter a mathematical expression: ")
    print("The postfix form of this formula is: {}".format(infix2postfix(string)))


if __name__ == "__main__":
    main()

