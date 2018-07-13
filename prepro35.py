"""Subject"""

def main():
    """main function"""
    num_a = int(input())
    num_b = int(input())
    num_c = int(input())
    num_d = int(input())
    num_e = int(input())

    print("%.2f" % parabola(num_a))
    print("%.2f" % parabola(num_b))
    print("%.2f" % parabola(num_c))
    print("%.2f" % parabola(num_d))
    print("%.2f" % parabola(num_e))

def parabola(num):
    """function"""
    numy = (((1/25)*num**2)-((6/5)*num)+9)
    return numy
main()
