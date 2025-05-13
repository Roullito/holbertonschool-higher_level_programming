#!/usr/bin/python3
def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None
    max_key = None
    for key in a_dictionary:
        if max_key is None or a_dictionary[key] > a_dictionary[max_key]:
            max_key = key
    return max_key
