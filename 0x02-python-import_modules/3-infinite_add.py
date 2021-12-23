#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add
    num = len(sys.argv)
    if num == 1:
        print("0")
    elif num > 1:
        x = int(sys.argv[1])
        for i in range(2, num):
            x += int(sys.argv[i])
        print("{}".format(x))
