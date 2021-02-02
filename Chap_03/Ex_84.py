# Coin Flip Simulation

# Flip simulated coins until either 3 consecutive faces occur, display the number of flips needed each time and the average number of flips needed

from random import choices

coins = ['H', 'T']

counter_tot = 0
for i in range(10):
    prev_flip = choices(coins)
    print(prev_flip[0], end=" ")

    counter = 1
    counter_line = 1
    while counter < 3:
        flip = choices(coins)
        if flip == prev_flip:
            counter += 1
        else:
            counter = 1
        prev_flip = flip
        print(prev_flip[0], end=" ")
        counter_line += 1
        if counter == 3:
            print(" ({} flips)".format(counter_line))
    counter_tot += counter_line

avg = counter_tot / 10
print("On average, {:.2f} flips were needed".format(avg))