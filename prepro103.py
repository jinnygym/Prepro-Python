"""pre-programming61"""
def main():
    """function"""
    alphabets_lower = 'abcdefghijklmnopqrstuvwxyz'
    alphabets_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    num = int(input())
    text = input()
    if text in alphabets_lower:
        print(alphabets_lower[0:27] - num)
    elif text in alphabets_upper:
        print(alphabets_upper[0:27] - num)
    else:
        print(text)
main()
