# Parity Bits (1 string per time)

# Compute the parity bit for groups of 8 bits entered by the user

bit = input("Enter the first bit: ")

while bit != "":
    if (bit.count("0") + bit.count("1") > 8) or len(bit) != 8:
        print("You have to enter 8 bits!!!")
    else:
        if bit.count("1") % 2 == 0:
            print("Parity bit should be: 0")
        else:
            print("Parity bit should be: 1")
    
    bit = input("Enter the a bit (blank to quit): ")