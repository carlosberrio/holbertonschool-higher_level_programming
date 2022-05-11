#!/usr/bin/python3
def roman_to_int(roman_string):

    if roman_string is None or type(roman_string) != str:
        return 0
    romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    for k in range(0, len(roman_string)):
        if k + 1 < len(roman_string) and romans[roman_string[k]] < romans[roman_string[k + 1]]:
            result -= romans[roman_string[k]]
        else:
            result += romans[roman_string[k]]
    return result
