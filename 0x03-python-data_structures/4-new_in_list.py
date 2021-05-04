#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    newList = list(my_list)
    if idx < 0:
        return (newList)

    if idx > len(my_list) - 1:
        return (newList)
    else:
        newList[idx] = element
        return (newList)
