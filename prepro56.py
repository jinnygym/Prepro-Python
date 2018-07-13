"""Good Afternoon"""
def main():
    """main function"""
    hour = int(input())
    minute = int(input())

    if hour >= 5 and hour < 12 and minute < 60:
        print("Good Morning")
    elif hour >= 12 and hour < 18 and minute < 60:
        print("Good Afternoon")
    elif hour >= 18 and hour < 23 and minute < 60:
        print("Good Evening")
    elif (hour >= 23 and hour < 24) or (hour >= 0 and hour < 5) and minute < 60:
        print("Good Night")
main()
