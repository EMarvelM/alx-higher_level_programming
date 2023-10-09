#!/usr/bin/python3
def no_c(my_string):
    myNew_str = ''
    for c in my_string:
        if c == "c" or c == "C":
            pass
        else:
            myNew_str += c
    return myNew_str
