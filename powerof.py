"""Power of X"""
def main():
    """function"""
    num = int(input())
    if num > 0:
        for i in range(0, num//2, 1):
            print("%s\\%s/%s" %(" " * (i), " " *(num-(i*2)-2), " " *(i)))
        for i in range(num//2, 0, -1):
            print("%s/%s\\%s" %(" " * (i-1), " " *((num-2)-(2*(i-1))), " " *(i-1)))

main()
