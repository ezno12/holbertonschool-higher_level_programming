#!/usr/bin/python3
def best_score(a_dictionary):
    max = ""
    k = 0
    if a_dictionary:
        for i, j in a_dictionary.items():
            if j > k:
                max = i
                k = j
        return max
    else:
        return None
