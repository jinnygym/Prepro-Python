"""Shabu"""
def main():
    """funtion"""
    price = float(input())
    service = price * 0.10
    vat = (service + price) * 0.08
    total = price + service + vat
    print("Price\t%.2f" % price, "THB")
    print("Service\t%.2f" % service, "THB")
    print("VAT\t%.2f" % vat, "THB")
    print("Total\t%.2f" % total, "THB")

main()
