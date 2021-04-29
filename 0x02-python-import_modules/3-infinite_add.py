#!/usr/bin/python3

import sys

def main(argv)
    add = 0
    for arg in sys.argv:
        if arg != sys.argv[0]:
            add += int(arg)

    print("{}".format(add))

if __name__ == "__main__":
    main()
