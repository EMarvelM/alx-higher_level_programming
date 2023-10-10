#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    lis = []
    tuple_a = list(tuple_a)
    tuple_b = list(tuple_b)
    for i in range(len(tuple_a)):
        try:
            tuple_b[i] >= 0
        except IndexError:
            tuple_b.append(0)
            
        lis += [tuple_a[i] + tuple_b[i]]
        tuple_c = tuple(lis)
    return tuple_c
