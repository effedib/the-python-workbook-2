# Text Messaging

# Display the key presses needed for a message entered by the user, using the cell phone numeric keypad.

keypad = {
    '.': '1', ',': '1'*2, '?': '1'*3, '!': '1'*4, ':': '1'*5,
    'A': '2', 'B': '2'*2, 'C': '2'*3,
    'D': '3', 'E': '3'*2, 'F': '3'*3,
    'G': '4', 'H': '4'*2, 'I': '4'*3,
    'J': '5', 'K': '5'*2, 'L': '5'*3,
    'M': '6', 'N': '6'*2, 'O': '6'*3,
    'P': '7', 'Q': '7'*2, 'R': '7'*3, 'S': '7'*4,
    'T': '8', 'U': '8'*2, 'V': '8'*3,
    'W': '9', 'X': '9'*2, 'Y': '9'*3, 'Z': '9'*3,
    ' ': '0'
}

string = input('Enter a string: ').upper()
for c in string:
    print(keypad[c], end='')
