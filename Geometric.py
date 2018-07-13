"""Geometric Sequence"""
def main():
    """main"""
    first = float(input())
    number = int(input())
    ratio = float(input())
    numi = 1
    while numi <= number:
        print("%.2f" % (first), end=" ")
        first *= ratio
        numi += 1
main()
