# Various examples


# constants = {"pi": 3.14, "e": 2.71, "root 2": 1.41}
# print(constants)


# results = {'pass': 0, 'fail': '0'}
# print(results)
# results['withdrawl'] = 1
# print(results)
# results['pass'] = 3
# results['fail'] = results['fail'] + '1'
# print(results)
# print('Fail = {}'.format(type(results['fail'])))
# print('Pass = {}'.format(type(results['pass'])))
# print(results['pass'])
# print(results['fail'])
# print(results['withdrawl'])
# a = results.pop('fail')
# print(results)
# print('a = {}'.format(a))
# print('lunghezza dizionario: {} elementi'.format(len(results)))
# if 'pass' in results:
#     print(results['pass'])
# if 1 in results.values():
#     print(results.keys())



# while loop example

# Count how many times each string is entered by the user
counts = {}

# Loop until 5 distinct strings have been entered
while len(counts) < 5:
    s = input("Enter a string: ")

    # if s is already a key in the dictionary then increase its count by 1. Otherwise add s to the dictionary with
    # a count of 1.
    if s in counts:
        counts[s] += 1
    else:
        counts[s] = 1

# Displays all of the strings and their counts
for k in counts:
    print('"{}" occurred "{}" times'.format(k, counts[k]))

