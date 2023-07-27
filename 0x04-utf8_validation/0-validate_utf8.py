#!/usr/bin/env python3
"""A module to validate UTF-8"""


def validUTF8(data):
    """ a method that determines if a given
    data set represents a valid UTF-8 encoding
    """
    k = len(data)
    checker = []
    for i in data:
        if i <= 128:
            checker.append(i)
    if k == len(checker):
        return True
    return False
