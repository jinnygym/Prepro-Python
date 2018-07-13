"""Equation I"""
import math
def main():
    """function"""
    num = float(input())
    out = 2 * math.log10(num) + num/3
    print("%.2f" %out)
main()
