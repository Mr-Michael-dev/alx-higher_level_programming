#!/usr/bin/python3

def best_score(a_dictionary):
    """returns a key wuth the biggest integer
    """
    if a_dictionary is None:
        return None
    else:
        max_val = max(a_dictionary, key=a_dictionary.get)
        return max_val
