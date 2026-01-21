#!/usr/bin/python3
"""
function that returns the key with the biggest integer value.
"""


def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None
    return max(a_dictionary, key=a_dictionary.get)
