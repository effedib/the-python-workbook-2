# Word by Word Palindromes

# This function reports if a string is or not a word by word palindrome

def wbwpalindrome(phrase: str) -> bool:
    from Ex_117 import onlywords

    phrase = phrase.lower()
    words = onlywords(phrase)
    final = len(words) - 1
    i = 0
    while i < ((len(words) - 1) / 2):
        if words[i] != words[final]:
            return False

        i += 1
        final -= 1

    return True


def main():
    s = input("Enter the string to verify if it's a word by word palindrome: ")
    is_palindrome = wbwpalindrome(s)
    if is_palindrome:
        print("The sentence entered is a word by word palindrome")
    else:
        print("The sentence entered isn't palindrome")


if __name__ == "__main__":
    main()
