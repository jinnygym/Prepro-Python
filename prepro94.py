"""Alphabet Sequence"""
def main():
    """function"""
    alpha = input()
    for i in range(ord("A"), ord("Z")+1):
        if chr(i) > alpha:
            break
        print(chr(i), end="")
    for i in range(ord("a"), ord("z")+1):
        if chr(i) > alpha:
            break
        print(chr(i), end="")
main()
