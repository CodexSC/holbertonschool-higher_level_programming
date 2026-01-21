#!/usr/bin/python3
"""
Find the max integer in a list
"""

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        return max(my_list)
