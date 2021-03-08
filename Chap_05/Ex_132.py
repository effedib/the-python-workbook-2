# Evaluate a Postfix

# This function evaluate a list in postfix form and display the result

from Chap_04.Ex_96 import isInteger
from Chap_05.Ex_131 import infix2postfix


def evaluatePostfix(string: str) -> int:
    postfix_token = infix2postfix(string)
    values = []
    for t in postfix_token:
        if isInteger(t):
            values.append(int(t))
        elif t == 'u-':
            converted = values.pop()
            converted = -converted
            values.append(converted)
        elif t in ['*', '/', '^', '+', '-']:
            right = values.pop()
            left = values.pop()
            if t == '*':
                result = left * right
            elif t == '/':
                result = left / right
            elif t == '^':
                result = left ** right
            elif t == '+':
                result = left + right
            elif t == '-':
                result = left - right
            values.append(result)

    return values[0]


def main():
    exp = input("Enter a mathematical expression: ")
    print("The result of this formula is: {}".format(evaluatePostfix(exp)))


if __name__ == "__main__":
    main()


