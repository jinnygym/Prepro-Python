"""Dogs Lover"""

def main():
    """main function"""
    total = 0
    price_a, price_b = int(input()), int(input())
    total += discount(price_a, price_b)
    price_a, price_b = int(input()), int(input())
    total += discount(price_a, price_b)
    price_a, price_b = int(input()), int(input())
    total += discount(price_a, price_b)
    price_a, price_b = int(input()), int(input())
    total += discount(price_a, price_b)
    print("%.2f" %total)

def discount(price_a, price_b):
    """function"""
    price_bf = price_a + price_b
    disc = price_bf * (15 / 100)
    total_price = price_bf - disc
    return total_price
main()
