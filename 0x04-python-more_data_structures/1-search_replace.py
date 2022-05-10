#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return [k if k != search else replace for k in my_list]
