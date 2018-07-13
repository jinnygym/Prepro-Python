"""No Vowels"""
def main():
    """main"""
    text = input()
    for i in text:
        if i in "AEIOUaeiou":
            continue
        else:
            print(i, end="")
main()
