#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print()
    for lis in matrix:
        for i in range(len(lis)):
            print(lis[i], end="")
            if i == (len(lis) - 1):
                print()
            else:
                print("", end=' ')
