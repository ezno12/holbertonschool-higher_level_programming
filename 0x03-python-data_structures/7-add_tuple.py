#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    alen = len(tuple_a)
    blen = len(tuple_b)
    if lena < 2:
        if alen == 0:
            tuple_a = (0, 0)
        else:
            tuple_a = (tuple_a[0], 0)
    if blen < 2:
        if blen == 0:
            tuple_b = (0, 0)
        else:
            tuple_b = (tuple_b[0], 0)
    a = tuple_a[0] + tuple_b[0]
    b = tuple_a[1] + tuple_b[1]
    tuple_c = (a, b)
    return tuple_c
