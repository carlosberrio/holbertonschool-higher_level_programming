#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    big = max(a_dictionary.items())
    return big[0]
