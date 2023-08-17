#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    keys = a_dictionary.keys()

    for key in keys:
        key = key.sorted()
        print(key)
