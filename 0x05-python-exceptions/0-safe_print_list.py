#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    j = 0
    #len of list
    for c in my_list:
        j += 1
    for i in range(x):
        if i >= j:
            print()
            return i
        print("{}".format(my_list[i]), end="")
    print()
    return x
