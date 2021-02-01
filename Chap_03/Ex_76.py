# Multiple Word Palindromes

# Extend the solution to EX 75 to ignore spacing, punctuation marks and treats uppercase and lowercase as equivalent in a phrase

# Make a tuple to recognize only the letters
letters = (
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
    "t", "u", "v", "w", "x", "y", "z"
)

# Read the sentence from the user
phrase = input("Enter a phrase: ").lower()

# Create a new string that contains only letters
new_phrase = ""
for c in phrase:
    if c in letters:
        new_phrase += c

# Analyse if the string is palindrome
final = len(new_phrase) - 1
is_palindrome = True
i = 0
while i < final:
    if new_phrase[i] != new_phrase[final]:
        is_palindrome = False
        break
    i       += 1
    final   -= 1

if is_palindrome is False:
    print("This phrase is not a palindrome!")
else:
    print("This phrase is palindrome!!")