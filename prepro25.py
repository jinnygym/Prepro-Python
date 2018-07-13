"""Middle Value"""
def main():
    """main function"""
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    max_ = max(num1, num2, num3)
    min_ = min(num1, num2, num3)
    total = num1 + num2 + num3
    print(total - max_ - min_)
main()
