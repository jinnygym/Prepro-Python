"""Speedtest"""
def main():
    """main speedtest"""
    fast1 = float(input())
    fast2 = float(input())
    fast3 = float(input())
    fast4 = float(input())
    fast5 = float(input())
    fast6 = float(input())

    highspeed = max(fast1, fast2, fast3, fast4, fast5, fast6)
    print("%.2f Mbps" %highspeed)
main()
