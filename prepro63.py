"""Basic Split Function"""
def main():
    """function"""
    numnum = float(input())
    num1 = "%.2f" %(numnum ** 2)
    num2 = "%.2f" %(numnum)
    num3 = "%.2f" %((2 * numnum) + 10)

    if numnum < 0:
        print(num1)
    elif numnum == 0:
        print(num2)
    elif numnum > 0:
        print(num3)
main()
