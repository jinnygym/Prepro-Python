"""pre-programming61"""
def main():
    """function"""
    text = ord(input())
    if text >= 65 and text <= 67:
        print(chr(text + 23))
    elif text >= 68 and text <= 90:
        print(chr(text - 3))
    elif text >= 97 and text <= 99:
        print(chr(text + 23))
    elif text >= 100 and text <= 122:
        print(chr(text - 3))
    else:
        print(chr(text))
main()
