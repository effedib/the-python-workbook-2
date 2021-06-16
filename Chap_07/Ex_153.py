# Find the Longest Word in a File
# Identify the longest word(s) in a file.
# Treat any group of non-white space characters as a word, even if includes digits o punct marks.

old_fname = input("Enter the name of a txt file: ")

try:
    old_file = open(old_fname, 'r', encoding='utf-8')

    # load the entire file in a list
    lines = old_file.read()

    # split the list using whitespaces (default in funct split)
    lines = lines.split()

    # initialize the list with longest words in the file
    longest_words = [lines[0]]

    for word in lines:
        # if we find a new longest word, newly initialize the list "longest_words"
        if len(word) > len(longest_words[0]):
            longest_words = [word]

        # if we find a same length, append the word
        elif len(word) == len(longest_words[0]):
            longest_words.append(word)

    print('Length of the longest word: {}'.format(len(longest_words[0])))
    print('Here is the longest words list: {}'.format(longest_words))
    old_file.close()

except FileNotFoundError:
    print("File not found.")
    quit()
