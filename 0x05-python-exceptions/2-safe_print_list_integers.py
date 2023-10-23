#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        print("{:d}".format(my_list[x]))
        return my_list[x]
    except (ValueError, TypeError):
        pass
