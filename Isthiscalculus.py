"""Is This Calculus?"""
def main():
    """main"""
    xxx = float(input())
    yyy = float(input())
    num_a = min(xxx, yyy)
    num_b = max(xxx, yyy)
    sol = ((num_b**3 / 3 + num_b) - (num_a**3 / 3 + num_a))
    print("%.2f" % sol)
main()