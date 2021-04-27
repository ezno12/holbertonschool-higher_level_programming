#!/usr/bin/python3
z = 1
for i in range(9):
    for j in range(i, 10):
        if z != 9:
            print('{:d}{:d}, '.format(i, j), end="")
        else:
            print('{:d}{:d}'.format(i, j))
    z += 1
