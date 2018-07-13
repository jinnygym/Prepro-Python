"""Health Record"""
def main(num):
    """function"""
    name = input()
    day = int(input())
    month = int(input())
    year = int(input())
    health_1(name, day, month, year, num)


def health_1(name, day, month, year, num):
    """function"""
    print("** Patient No.%d **" %num)
    print("Full Name: %s" %name)
    print("Birthday:  %d/%d/%d\n" %(day, month, year))

main(1)
main(2)
main(3)
main(4)
main(5)
