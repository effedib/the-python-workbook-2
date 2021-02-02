# Maximum Integer

# Generate randomly a collection of integers that contains numbers between 1 to 100 and find the maximum value displaying each update in a row

from random import randint

counter = 0
num_prev = randint(1, 100)
print(num_prev)
for i in range(1, 100):
    num = randint(1, 100)
    if num > num_prev:
        num_prev = num
        counter += 1
        print(num_prev, "<== Update")
    else:
        print(num)
print("\nThe maximum value found was {}".format(num_prev))
print("\nThe maximum value was updated {} times".format(counter))

