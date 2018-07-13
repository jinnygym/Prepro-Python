"""Password Validation"""
def main():
    """main function"""
    text = input()

    if len(text) >= 8:
        print("Password is valid, you can use this password.")
    else:
        print("Password too short, try again.")
main()
