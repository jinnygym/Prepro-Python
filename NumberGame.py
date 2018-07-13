"""Number Game"""
def main():
    """main"""
    num0 = int(input())
    num1 = int(input())
    num01 = int(input())
    num2 = int(input())
    num02 = int(input())
    num3 = int(input())
    num03 = int(input())
    player1 = abs(num1 + num2 + num3 - num0)
    player2 = abs(num01 + num02 + num03 - num0)

    if player1 < player2:
        print("Saint won!")
    elif player1 > player2:
        print("Gunn won!")
    else:
        print("Draw!")
main()
