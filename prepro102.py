"""pre-programming61"""
def main():
    """function"""
    text = ord(input())
    if text >= 88 and text <= 90:
        print(chr(text - 23))
    elif text >= 65 and text <= 87:
        print(chr(text + 3))
    elif text >= 120 and text <= 122:
        print(chr(text - 23))
    elif text >= 97 and text <= 119:
        print(chr(text + 3))
    else:
        print(chr(text))
main()
