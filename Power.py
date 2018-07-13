"""Power of X"""
def main():
    """main"""
    num = int(input())
    for i in range(num//2):
        print(i* " " + "\\")
    for k in range(num//2):
        print(((num-1)-k)*" " +"/")
main()
