#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    lis = []
    tuple_a = list(tuple_a)
    tuple_b = list(tuple_b)
    if len(tuple_a) > len(tuple_b):
        lent = len(tuple_a)
    else:
        lent = len(tuple_b)
    for i in range(lent):
        if i < 2:
            try:
                tuple_b[i] >= 0
            except IndexError:
                tuple_b.append(0)

            lis += [tuple_a[i] + tuple_b[i]]
            tuple_c = tuple(lis)
        else:
            pass
    return tuple_c
