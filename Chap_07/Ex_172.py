# Words with Six Vowels in Order

vowels = 'aeiouy'
# vowels = ('a', 'e', 'i', 'o', 'u', 'y')

file = input('Enter the name of the file to search if it contains words with six vowels in order: ')

try:
    with open(file, 'r', encoding='utf-8') as fin:

        vowels_word = []

        for line in fin:
            word_lst = line.lower().split()
            for word in word_lst:
                verify = ''
                for char in word.lower():
                    if char in vowels:
                        verify += char
                if verify == vowels:
                    vowels_word.append(word)


except:
    print('An error occurred accessing or processing the file')
    print('Quitting...')
    quit()


print(vowels_word)
