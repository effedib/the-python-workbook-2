# Center a String in the Terminal Window

# This function takes a string and the width of the window in characters as its parameters
# and returns a new string after how many spaces are needed so that the string will be centered in the window when is printed.

def centerString(string: str, width: int) -> str:
    if len(string) >= width:
    
        return string
    
    spaces      = (width - len(string) // 2)
    newString   = " " * spaces + string

    return newString

def main():
    width = 100
    print(centerString("Harry", width))
    print(centerString("Potter", width))
    print(centerString("is", width))
    print(centerString("my", width))
    print(centerString("favourite", width))
    print(centerString("book", width))

main()
