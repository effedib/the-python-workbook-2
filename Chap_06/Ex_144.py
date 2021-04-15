# Anagrams Again

# Determine if two phrases are anagrams ignoring capitalization, punctuation marks and spacing


def is_anagram(phrase1: str, phrase2: str) -> bool:
    punctuation_marks = ['.', ',', '!', ':', ';', '?', "'", ' ']
    characters1 = dict()
    characters2 = dict()
    phrase1, phrase2 = (phrase1.lower(), phrase2.lower())

    for c in phrase1:
        if c not in punctuation_marks:
            if c in characters1:
                characters1[c] += 1
            else:
                characters1[c] = 1

    for c in phrase2:
        if c not in punctuation_marks:
            if c in characters2:
                characters2[c] += 1
            else:
                characters2[c] = 1

    if characters1 == characters2:

        return True

    return False


def main():
    string1 = input("Enter the first string to control: ")
    string2 = input("Enter the second string to control: ")

    if is_anagram(string1, string2):
        print("Compliments! They are anagrams!")
    else:
        print("They aren't anagrams!")


if __name__ == "__main__":
    main()
