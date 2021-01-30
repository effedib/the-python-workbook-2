# Fizz-Buzz

# Display the answers for the first 100 numbers in the Fizz-Buzz game

for i in range(100):
    if (i % 3 == 0) and (i % 5 == 0):
        i = 'Fizz-Buzz'
    elif i % 3 == 0:
        i = "Fizz"
    elif i % 5 == 0:
        i = "Buzz"
    print(i)