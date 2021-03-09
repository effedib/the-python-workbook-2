# The Sieve of Eratosthenes

# Simulate the Eratosthenes algorithm to find al the prima numbers between 2 and a limit entered by the user.


limit = int(input('Enter a limit number to calculate all of the\nprime numbers between 2 and your number limit: '))

prime_list = [n for n in range(limit+1)]

# My solution = slow
# for p in prime_list:
#     if p not in [0, 1]:
#         for pp in range(prime_list.index(p), limit+1):
#             if prime_list[pp] % p == 0 and prime_list[pp] != p:
#                 prime_list[pp] = 0

# Workbook solution = very fast
p = 2
while p < limit:
    for i in range(p*2, limit+1, p):
        prime_list[i] = 0
    p += 1
    while p == 0 and p < limit:
        p += 1

prime_list = [z for z in prime_list if z > 1]

print('The prime number are: {}'.format(prime_list))

