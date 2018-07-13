"""prepro61"""
def main():
    """function"""
    matrix = list()
    row_amount, col_amount = int(input()), int(input())

    for _ in range(row_amount):
        matrix.append([])
        for _ in range(col_amount):
            matrix[-1].append(int(input()))

    for i in matrix:
        for j in i:
            print(j, end=" ")
        print()

main()
