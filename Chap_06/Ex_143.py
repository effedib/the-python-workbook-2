# Anagrams

# Determine if two strings are anagrams and display the result.

characters = dict()

string1 = input("Enter the first string to control: ")
string2 = input("Enter the second string to control: ")


if len(string1) != len(string2):

    anagrams = False

else:

    anagrams = True

    for c in string1:
        characters[c] = False

    for c in string2:
        characters[c] = True

    for c in characters:
        if characters[c] is False:
            anagrams = False

if anagrams is True:
    print("Compliments! They are anagrams!")
else:
    print("They aren't anagrams!")
