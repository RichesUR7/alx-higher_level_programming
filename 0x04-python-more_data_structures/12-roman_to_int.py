#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or not isinstance(roman_string, str):
        return 0
    rv = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    for i in range(len(roman_string)):
        if i > 0 and rv[roman_string[i]] > rv[roman_string[i - 1]]:
            result += rv[roman_string[i]] - 2 * rv[roman_string[i - 1]]
        else:
            result += rv[roman_string[i]]
        return roman_n
