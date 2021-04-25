# Recursive Palindrome

# This recursive function determines whether or not a string is palindrome


def recursive_ispalindrome(string: str) -> bool:

    not_alpha = ["'", ",", "-", ".", "?", "!", ":", ";", " "]

    if string == '' or len(string) == 1:

        return True

    elif string[0] in not_alpha:

        return recursive_ispalindrome(string[1:])

    elif string[len(string)-1] in not_alpha:

        return recursive_ispalindrome(string[:len(string)-1])

    elif string[0] == string[len(string)-1]:

        return recursive_ispalindrome(string[1:(len(string)-1)])

    else:

        return False


def main():
    palin_word = input("Enter a word: ")

    if recursive_ispalindrome(palin_word) is False:
        print("This phrase is not a palindrome!")
    else:
        print("This phrase is palindrome!!")


if __name__ == '__main__':
    main()
