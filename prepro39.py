"""Name list"""
def main():
    """function"""
    start = int(input())
    name(start)
    name(start+5)
    name(start+10)
    name(start+15)
    name(start+20)
    name(start+25)
    name(start+30)
    name(start+35)
    name(start+40)
    name(start+45)


def name(start):
    """main function"""
    name_a = input()
    name_b = input()
    name_c = input()
    name_d = input()
    name_e = input()

    print("ID#%d\t%s" % (start, name_a))
    print("ID#%d\t%s" % (start+1, name_b))
    print("ID#%d\t%s" % (start+2, name_c))
    print("ID#%d\t%s" % (start+3, name_d))
    print("ID#%d\t%s" % (start+4, name_e))

main()
