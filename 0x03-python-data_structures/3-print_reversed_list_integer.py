#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    i = len(my_list)
    reversed_list = my_list[i - 1::-1]

    for num in reversed_list:
        print("{:d}".format(num))
