"""Word Game"""
def main(text, score=100):
    """function"""
    for _ in range(20):
        keep = input()
        if keep == text:
            print("Correct!! You've %s points remaining." %score)
            break
        elif keep != text:
            score -= 5
    if score == 0:
        print("Game Over!")

main(input())
