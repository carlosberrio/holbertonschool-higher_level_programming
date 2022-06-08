#!/usr/bin/python3
'''print sorted
'''


class MyList(list):
    """subclass of list"""
    def print_sorted(self):
        """prints the sorted list"""
        print(sorted(self))