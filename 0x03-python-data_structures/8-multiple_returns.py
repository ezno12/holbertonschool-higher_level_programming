#!/usr/bin/python3
def multiple_returns(sentence):
    lenSen = len(sentence)
    if (lenSen == 0):
        return (0, None)
    return (lenSen, sentence[0])
