#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    c = 0
    for idx in range(x):
        try:
            print(my_list(idx), end="")
            c += 1
        except:
            pass
    print("")
    return c
