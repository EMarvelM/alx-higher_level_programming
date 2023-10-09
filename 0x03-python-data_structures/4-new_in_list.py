#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx >= 0 and idx < len(my_list):
        myNew_list = []
        for i in range(len(my_list)):
            if i == idx:
                myNew_list.append(element)
            else:
                myNew_list.append(my_list[i])
        return myNew_list
    else:
        return my_list
