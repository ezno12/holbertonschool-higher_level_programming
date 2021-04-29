#!/usr/bin/python3
import sys
"""
   program print the number of the list argument

   arg:
     argv: inputed arg
"""
def main(*argv):
    i = 0
    lenth = len(sys.argv) - 1
    if lenth == 1:
        print("{:d} argument:".format(lenth))
    elif lenth == 0:
        print("{:d} arguments.".format(lenth))
    else:
        print("{:d} arguments:".format(lenth))
    for args in sys.argv:
        if (i != 0):
            print("{}: {}".format(i, args))
        i += 1

if __name__ == "__main__":
    main()
