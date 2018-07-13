"""Power of X"""
def main():
    """main"""
    num = int(input())
    for i in range(num//2):
        print(" "*(i)+"\\"+" "*((num//2)-(1*2))+"/")
    for k in range(num//2):
        print(" "*((num//2)-k-i)+"/"+" "*(2*k)+"\\")
main()
