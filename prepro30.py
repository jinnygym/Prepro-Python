"""Introduction to Calculus"""
import math
def main():
    """function"""
    num1 = int(input())
    num2 = int(input())
    numa = min(num1, num2)
    numb = max(num1, num2)
    out = ((-(3/2)*math.cos(2*numb/3)-math.sin(numb)+4*numb) - \
        ((-(3/2)*math.cos(2*numa/3)-math.sin(numa)+4*numa)))
    print("%.2f" %out)
main()
