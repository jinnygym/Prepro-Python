"""Memorial"""
import math
def main():
    """function"""
    num = float(input())
    high = float(input())
    num_ = num / 2
    total = ((1/3) * math.pi * num_ **2 * high)
    print("%.3f" %total)
main()
