# Pig Latin

from Ex_117 import onlywords

vowels = ['a', 'e', 'i', 'o', 'u', 'y']

eng_str = input("Enter a sentence in english: ")

eng_list = onlywords(eng_str)
pig_list = []
for string in eng_list:
    if string[0] in vowels:
        new_string = str(string) + 'way' + ' '
        pig_list.append(new_string)
    else:
        new_string = str(string[1:]) + str(string[0]) + 'ay' + ' '
        pig_list.append(new_string)

pig_str = "".join(pig_list).rstrip()

print(pig_str)
