"""Digital Clock"""
def main():
    """function"""
    hour, minute = int(input()), int(input())

    if hour < 0 or hour > 23 or minute < 0 or minute > 59:
        print("Invalid Time")
    elif 0 <= hour <= 11:
        print("%d:%02d AM" % (hour, minute))
    elif hour == 12:
        print("%d:%02d PM" % (hour, minute))
    elif 13 <= hour <= 23:
        hour -= 12
        print("%d:%02d PM" % (hour, minute))
main()
