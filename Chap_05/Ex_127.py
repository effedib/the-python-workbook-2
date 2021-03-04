# Is a List already in Sorted Order?

# Read a list of numbers from the user and report whether or not a list is sorted

def is_sorted(n_list: list) -> bool:

    copy_list = n_list[:]
    copy_list.sort()
    copy_list.reverse()
    if n_list == []:
        return 'Empty list'
    elif n_list == copy_list:
        return True
    elif n_list == sorted(n_list):
        return True

    return False


num = input("Enter the first number: ")

num_list = []
while num != '':
    num_list.append(float(num))
    num = input("Enter the next number (blank to quit): ")

print(is_sorted(num_list))