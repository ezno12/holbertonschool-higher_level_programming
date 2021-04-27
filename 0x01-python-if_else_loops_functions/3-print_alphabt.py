#!/usr/bin/python3
# Print lowercase expect e and q
for c in range(97, 123):
    if chr(c) != 'q' and chr(c) != 'e':
        print("{}".format(chr(c)), end="")
