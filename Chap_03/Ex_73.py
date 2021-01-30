# Caesar Cipher

# Implement a Caesar Cipher to encode and decode messages

letters = (
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
    "t", "u", "v", "w", "x", "y", "z"
)

message = input("Enter the message: ")
shift   = int(input("Enter the number of letters to shift: "))

new_message = ""
for c in message:
    if c in letters:
        index = letters.index(c) + shift
        new_letter = letters[index]
        new_message += new_letter
    elif 'A' <= c <= 'Z':
        index = ord(c) - ord('A')
        index = (index + shift) % 26
        new_letter = chr(index + ord('A'))
        new_message += new_letter
    else:
        new_message += str(c)

print("Message shifted: {}".format(new_message))