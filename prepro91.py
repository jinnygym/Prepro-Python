"""Summation"""
def main():
    """function"""
    num1 = int(input())
    keep = 0

    for _ in range(num1):
        num2 = float(input())
        keep += num2
    print("%.4f" % keep)
main()
