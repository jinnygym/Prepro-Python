"""Last Digit"""
def main():
    """function"""
    price1 = int(input())
    price2 = int(input())
    full = price1 + price2
    ser = full * 0.09
    vat = (full + ser) * 0.075
    total = full + ser + vat
    print("Total: %.2f" %(full), "THB")
    print("Service: %.2f" %(ser), "THB")
    print("VAT: %.2f" %(vat), "THB")
    print("Final Price: %.2f" %(total), "THB")
main()
