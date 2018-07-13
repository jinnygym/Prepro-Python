"""Arithmetic Sequence"""
def main():
    """main function"""
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())

    for i in range(num1, num3-1, num2):
        print(i)

main()
