#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list:
        for k in reversed(my_list):
            print(k, end="\n")
