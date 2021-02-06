# Capitalize It

# This function takes a string as its only parameter and returns a new copy of the string that has been correctly capitalized.

def Capital(string: str) -> str:
    marks = (".", "!", "?")
    new_string = ""
    first = True
    for i, c in enumerate(string):
        if c != " " and first is True:
            first = False
            new_string += c.capitalize()
        elif c in marks:
            new_string += c
            first = True
        elif c == 'i' and (string[i-1]) == ' ' and (string[i+1] == ' ' or string[i+1] in marks):
            new_string += c.capitalize()
        else:
            new_string += c
    
    return new_string

stringa = input("Inserisci una frase: ")
print(Capital(stringa))