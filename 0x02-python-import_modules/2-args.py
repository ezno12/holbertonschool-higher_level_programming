#!/usr/bin/python3
import sys
"""
   program print the number of the list argument

   arg:
     argv: inputed arg
"""
def main():
    argv = sys.argv
    i = 0
    lenth = len(argv) - 1
    if len(argv) == 1:
        print("0 argument.")
    else:
        print(lenth," argement: ")
        for args in sys.argv:
            if( i != 0):
                print("{:d}: {}".format(i,argv[i]))
            i += 1
if __name__ == '__main__':
    main()
