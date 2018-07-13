"""Broken Watch"""
def main():
    """function"""
    times_1 = int(input())
    times_2 = int(input())
    times_3 = int(input())
    t_hrs = times // 3600
    t_hrs_ = times % 3600
    t_mins = t_hrs_ // 60
    t_mins_ = t_hrs_ % 60
    print(("%i Hour(s) %i Minute(s) %i Second(s)") % (t_hrs, t_mins, t_mins_))
    print(("%i Hour(s) %i Minute(s) %i Second(s)") % (t_hrs, t_mins, t_mins_))
    print(("%i Hour(s) %i Minute(s) %i Second(s)") % (t_hrs, t_mins, t_mins_))
main()
