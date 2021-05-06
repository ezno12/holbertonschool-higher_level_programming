#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    Sorted_Dic = sorted(a_dictionary.keys())
    for i in Sorted_Dic:
        print("{}: {}".format(i, a_dictionary[i]))
