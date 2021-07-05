# Weird Words
# Verify if a word respects the rule "I before E except after C".

def findWeirdWords(file: str) -> tuple:

    try:
        fin = open(file, 'r', encoding='utf-8')

    except:
        print('A problem was encountered while opening the file!')
        print('Quitting...')
        quit()

    lines = fin.read()
    # split the file in words
    lines = lines.split()

    # create two sets because we don't want repeated elements and they are very fast to process
    rule_set = set()
    unrule_set = set()
    for line in lines:
        if line not in rule_set and line not in unrule_set:
            if 'cei' in line:
                rule_set.add(line)
            elif 'ie' in line:
                if 'cie' in line:
                    unrule_set.add(line)
                else:
                    rule_set.add(line)
            elif 'ei' in line:
                unrule_set.add(line)

    return rule_set, unrule_set


def main():
    finput = input('Enter the name of the file to process: ')

    rules, unrules = findWeirdWords(finput)

    print('Here is the list of the words that follow the rule:\n{}\n'.format(rules))
    print('Rule set: {}\n'.format(len(rules)))
    print('Here is the list of the words that don\'t follow the rule:\n{}\n'.format(unrules))
    print('Violating rule set: {}'.format(len(unrules)))


if __name__ == '__main__':
    main()
