"""BTS Skytrain EP.1"""
def main():
    """main function"""
    coin5 = int(input())

    if coin5 >= 4:
        print("Mo Chit (N8)")
        print("Saphan Khwai (N7)")
    if coin5 >= 6:
        print("Ari (N5)")
        print("Sanam Pao (N4)")
    if coin5 >= 7:
        print("Victory Monument (N3)")
    if coin5 >= 8:
        print("Phaya Thai (N2)")
        print("Ratchathewi (N1)")
    if coin5 >= 9:
        print("Siam (CEN)")
    else:
        print(" ")
main()
