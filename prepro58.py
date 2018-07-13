"""MRT Blue Line"""
def main():
    """main function"""
    name = input()
    type_ = input()

    if type_ == "Adult":
        mrt_station(name, 21, 23, 25, 28)
    if type_ == "Student":
        mrt_station(name, 19, 21, 23, 25)
    if type_ == "Elder":
        mrt_station(name, 11, 12, 13, 14)

def mrt_station(name, aaa, bbb, ccc, ddd):
    """function"""
    if name == "Chatuchak Park":
        print(aaa)
    elif name == "Phahon Yothin":
        print(bbb)
    elif name == "Lat Phrao":
        print(ccc)
    elif name == "Ratchadaphisek":
        print(ddd)
main()
