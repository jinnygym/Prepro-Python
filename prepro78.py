"""Lane"""
def main():
    """function"""
    lane = 1
    turn = ""
    while turn != "P":
        turn = input()
        if turn == "L" and lane == 1:
            lane = 1
        elif turn == "R" and lane == 1:
            lane = 2
        elif turn == "L" and lane == 2:
            lane = 1
        elif turn == "R" and lane == 2:
            lane = 3
        elif turn == "L" and lane == 3:
            lane = 2
        elif turn == "R" and lane == 3:
            lane = 4
        elif turn == "L" and lane == 4:
            lane = 3
        elif turn == "R" and lane == 4:
            lane = 4
    print(lane)

main()
