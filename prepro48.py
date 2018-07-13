"""The Edge"""
def main():
    """function"""
    num1 = float(input())
    num2 = float(input())
    num3 = float(input())
    num4 = float(input())
    num5 = float(input())
    total = num1 + num2 + num3 + num4 + num5
    max_ = max(num1, num2, num3, num4, num5)
    min_ = min(num1, num2, num3, num4, num5)
    aver = total / 5
    print("Total: %.2f" %(total), "THB")
    print("Maximum: %.2f" %(max_), "THB")
    print("Minimum: %.2f" %(min_), "THB")
    print("Average: %.2f" %(aver), "THB")
main()
