"""Pancake"""
def main():
    """function"""
    amo, extra, demand = int(input()), int(input()), int(input())
    pack = amo + extra

    pay, get = 0, 0
    while demand >= pack:
        get += pack
        pay += amo * 20
        demand -= pack

    if demand < amo:
        get += demand
        pay += demand * 20

    elif demand >= amo:
        get += pack
        pay += amo * 20

    print("Pay:", pay)
    print("Get:", get)

main()
