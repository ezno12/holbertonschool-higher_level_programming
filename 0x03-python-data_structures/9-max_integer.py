#!/usr/bin/python3
def max_integer(my_list=[]):
    ListLen = len(my_list)
    if (ListLen == 0):
        return None
    Biggest = my_list[0]
    for i in my_list:
        if i > Biggest:
            Biggest = i
    return (Biggest)
