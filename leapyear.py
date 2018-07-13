"""Leap Year"""
def main():
    """main function"""
    year = int(input())

    if (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)) and year > 0:
        print("%d is leap year." %year)
    elif year % 400 != 0 and year > 0:
        print("%d is not leap year." %year)
    else:
        print("This year does not exist.")
main()
