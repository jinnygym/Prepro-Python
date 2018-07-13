"""Every once in a while"""
def main():
    """main function"""
    num2 = int(input())
    numk = int(input())
    if num2 > 0:
        for i in range(1, num2+1, numk):
            print(i)
    elif num2 < 0:
        for j in range(-1, num2-1, -numk):
            print(j)
main()
