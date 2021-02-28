# Formatting a List

# This function takes a list of strings and returns an only string that contains all of the items in the list,
# formatted with commas and an "and" before the last item.

def format_list(list_str: list) -> str:
    new_list = list_str[0:1]
    for i in range(1, len(list_str)-1):
        new_list.append(', ')
        new_list.append(list_str[i])
    new_list.append(' and ')
    new_list.append(list_str.pop())

    return ''.join(new_list)


def main():
    item = input("Enter the first item: ")

    ls = []
    while item != '':
        ls.append(item)
        item = input("Enter the next item (blank to quit): ")

    print("The list you entered is composed by:")
    print(format_list(ls))


if __name__ == "__main__":
    main()
