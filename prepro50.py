"""cola"""
import math
def main():
    """main function"""
    num1 = function()
    num2 = function()
    num3 = function()
    num4 = function()
    num5 = function()
    total = num1 + num2 + num3 + num4 + num5
    print("Total %.2f ml." % total)

def function():
    """call function"""
    radius1 = float(input())
    high1 = float(input())
    keep = math.pi * (radius1 ** 2) * high1
    return keep

main()
