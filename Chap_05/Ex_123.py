# Pig Latin Improved

from re import split
from Ex_117 import onlywords

vowels = ['a', 'e', 'i', 'o', 'u', 'y']
punctuation_marks = [',', '.', '?', '-', "'", '!', ':', ';']

eng_str = input("Enter a sentence in english: ")

eng_list = split(' ', eng_str)
pig_list = []
for string in eng_list:
    if string[0].lower() in vowels:
        if string[len(string)-1] in punctuation_marks:
            pun = string[len(string)-1]
            new_string = str(string[:len(string)-1]) + 'way' + pun + ' '
        else:
            new_string = str(string) + 'way' + ' '
        pig_list.append(new_string)
    else:
        if string[0].islower():
            if string[len(string) - 1] in punctuation_marks:
                pun = string[len(string) - 1]
                new_string = str(string[1:len(string)-1]) + str(string[0]) + 'ay' + pun + ' '
            else:
                new_string = str(string[1:len(string)-1]) + str(string[0]) + 'ay' + ' '
            pig_list.append(new_string)
        else:
            if string[len(string) - 1] in punctuation_marks:
                pun = string[len(string) - 1]
                new_string = str(string[1:len(string)-1]).capitalize() + str(string[0]).lower() + 'ay' + pun + ' '
            else:
                new_string = str(string[1:len(string)-1]).capitalize() + str(string[0]).lower() + 'ay' + ' '
            pig_list.append(new_string)

pig_str = "".join(pig_list).rstrip()

print(pig_str)
