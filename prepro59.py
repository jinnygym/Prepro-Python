"""The Camp EP.2 "Pick Day Pick Me Up!"""
def main():
    """main function"""
    num = int(input())

    if 23 <= num <= 25:
        print("Yep! %d UNiTEC@MP3" %num)
    elif num >= 1 and num < 23 or num > 25 and num <= 31:
        print("Try again!")
    else:
        print("404 NOT FOUND")
main()
