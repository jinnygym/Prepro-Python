"""Change"""
def main():
    """function"""
    money = int(input())
    price = int(input())
    change = money - price

    bank100 = change // 100
    bank50 = (change % 100) // 50
    bank20 = (change % 100) % 50 // 20
    coin10 = (change % 100) % 50 % 20 // 10
    coin5 = (change % 100) % 50 % 20 % 10 // 5
    coin2 = (change % 100) % 50 % 20 % 10 % 5 // 2
    coin1 = (change % 100) % 50 % 20 % 10 % 5 % 2 // 1

    print(bank100)
    print(bank50)
    print(bank20)
    print(coin10)
    print(coin5)
    print(coin2)
    print(coin1)

main()
