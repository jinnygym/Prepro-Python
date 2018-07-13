"""Equation II"""
import math
def main():
    """function"""
    num = float(input())
    out = (math.sin(math.radians(3*num))) + abs(num/4)+5
    print("%.2f" %out)
main()
