# Vowel or Consonant

# Read a letter from the user
letter = input("Enter a letter of the alphabet: ")
letter = letter.lower()

# Analyse if it's a vowel and display the result
if letter == 'y':
    print("This letter 'Y' sometimes is a vowel and sometimes is a consonant.")
elif letter in ['a','e','i','o','u']:
    print("The entered letter is a vowel.")
else:
    print("The entered letter is a consonant.")