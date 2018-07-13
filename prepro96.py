"""Spear"""
def main():
    """function"""
    num = int(input())//2 + 1
    for i in range(1, num+1):
        print(" "*(num-i) + "*" + " "*(2*i-3) + "*"*(i != 1))
    for i in range(num-1, 0, -1):
        print(" "*(num-i) + "*" + " "*(2*i-3) + "*"*(i != 1))

    for _ in range(num*2-1):
        print(" "*(num-1) + "*")
main()
