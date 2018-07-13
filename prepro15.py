"""Donut Area"""
def main():
    """funtion"""
    numbig = int(input())
    numsmall = int(input())
    donutbig = 3.14 * numbig **2
    donutsmall = 3.14 * numsmall **2
    total = (donutbig - donutsmall)
    print("Donut Area is %.2f" % total + "!")
main()
