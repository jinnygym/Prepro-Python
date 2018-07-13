"""Box"""
def main():
    """main"""
    num_1 = int(input())
    if num_1 == 1:
        print("*")
    else:
        print("* "*num_1)
        for _ in range(num_1-2):
            print("*" + " " * (num_1-2)+ " " * (num_1-1) + "*")
        print("* "*num_1)
main()
