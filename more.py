"""More Split Function"""
import math
def main():
    """function"""
    num = float(input())
    num2 = (math.radians(num))
    if num <= 0:
        number_1 = "%.2f"%(abs(num)**(-(1/2)*num))
        print(number_1)
    elif 0 < num <= 2:
        number_2 = "%.2f"%(12 * math.pi * num)
        print(number_2)
    elif num > 2:
        number_3 = "%.2f"%(((2**num*math.sin(num2)) + math.sqrt(num))/2)
        print(number_3)
main()
