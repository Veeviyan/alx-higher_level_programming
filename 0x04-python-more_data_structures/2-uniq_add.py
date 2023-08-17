#!/usr/bin/python3

def uniq_add(my_list=[]):
    unique_int = []
    result = 0

    if my_list:
        for i in set(my_list):
            if i not in unique_int:
                result = i + result
        return (result)
