"""prepro61"""
def main():
    """function"""
    data = list()
    amount = int(input())
    for  i  in range(amount):
        name = input()
        score = int(input())
        data.append([score, name])

    for i in sorted(data):
        print(i[0], i[1])
main()
