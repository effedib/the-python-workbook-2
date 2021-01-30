# Is a String a Palindrom

# Determine if a string is palindrome

word = input("Enter a word: ")

final = len(word) - 1

is_palindrome = True
i = 0
while i < ((len(word) - 1) / 2):
    if word[i] != word[final]:
        is_palindrome = False
        break
    i       += 1
    final   -= 1

if is_palindrome is False:
    print("This word is not a palindrome!")
else:
    print("This word is palindrome!!")