#!/usr/bin/python3
def remove_char_at(str, n):
    s = ''
    i = 0
    for char in str:
        if i != n:
            s += str[i]
        i += 1
    return (s)
