#!/usr/bin/python3
"""
find the peak in unsorted list of integer
time complexity: O(log(n))
space complexity: O(1)
"""


def find_peak(list_of_integers):
    peak = sorted(list_of_integers)[-2]
    return peak
