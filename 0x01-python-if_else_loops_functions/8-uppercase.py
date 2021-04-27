#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if (ord(str[c]) >= 97 and ord(str[c]) <= 122):
           c = ord(str[c]-32)
        print("{}".format(c), end="")
print("")
