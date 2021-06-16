# Number the Lines in a File
# Read lines from a file and write them info a new file, preceded by the line number.

old_fname = input("Enter the name of a txt file: ")
new_fname = input("Enter the name of the new file: ")

old_file = open(old_fname, 'r', encoding='utf-8')
new_file = open(new_fname, 'w', encoding='utf-8')

old_lines = old_file.readlines()

for i, line in enumerate(old_lines):
    new_file.write('{}: {}'.format(i+1, line))

old_file.close()
new_file.close()

print('File copied successfully')
