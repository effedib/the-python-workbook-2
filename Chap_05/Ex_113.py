# Avoiding Duplicates

# Read words from the user and display each word entered exactly once

# Read the first word from the user
word = input("Enter a word (blank to quit): ")

# Create an empty list
list_words = []

# Loop to append words into the list until blank is entered and if is not a duplicate
while word != '':
    if word not in list_words:
        list_words.append(word)
    word = input("Enter another word (blank to quit): ")

# Display the result
for word in list_words:
    print(word)
