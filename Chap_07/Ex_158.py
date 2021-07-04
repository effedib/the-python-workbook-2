# Remove Comments
# Remove all of the comments from a python source file and save the modified file using a new name.

def remove_comments(file: str, new_file: str):
    print('Opening Files')

    try:
        fin = open(file, 'r', encoding='utf-8')

    except:
        print('A problem was encountered with the input file!')
        print('Quitting...')
        quit()

    try:
        fout = open(new_file, 'w')

    except:
        print('A problem was encountered with the output file!')
        fin.close()
        print('Quitting...')
        quit()

        print('Beginning cleaning')

    try:
        # first char to begin clean the line
        target = '#'

        for line in fin:
            index = line.find(target)
            if index > -1:
                line = line[:index]
                line += '\n'

            # write only the code without the target parameters and the next chars
            fout.write(line)

        fin.close()
        fout.close()

        print('File cleaned')

    except:
        print('A problem was encountered while processing the file!')
        fin.close()
        fout.close()
        quit()


def main():
    f_source = input('Enter the name of a file to clean from comments: ')
    f_output = input('Enter the name of a clean file to create: ')
    remove_comments(f_source, f_output)


if __name__ == '__main__':
    main()
