#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx >= 0 and idx < len(my_list):
        myNew_list = my_list
        myNew_list[idx] = element
        return myNew_list
    else:
        return my_list
