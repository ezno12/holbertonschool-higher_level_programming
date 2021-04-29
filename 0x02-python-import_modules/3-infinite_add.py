#!/usr/bin/python3
import sys
"""
   program print the number of the list argument

   arg:
     argv: inputed arg
"""
argv = sys.argv
if len(argv) == 1:
    print("0 argument.")
else:
    print(len(argv)," argement: ")
    for i in range(len(argv)):
        
        print("{:d}: {}".format(i+1,argv[i+1]))

