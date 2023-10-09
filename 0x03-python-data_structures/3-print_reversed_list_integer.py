#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for num in reversed(sorted(my_list)):
        print("{:d}".format(num))
