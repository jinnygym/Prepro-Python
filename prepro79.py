"""Kangaroo"""
def main():
    """function"""
    pos_1, jump1 = int(input()), int(input())
    pos_2, jump2 = int(input()), int(input())

    if jump1 <= jump2:
        print("NO")

    elif jump1 > jump2:
        while pos_1 < pos_2:

            pos_1 += jump1
            pos_2 += jump2
        if pos_1 == pos_2:
            print("YES")
        elif pos_1 > pos_2:
            print("NO")
main()
