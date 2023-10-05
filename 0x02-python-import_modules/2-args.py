#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    if len(argv) == 1:
        print("{0:d} arguments.".format(len(argv) - 1))
    elif len(argv) == 2:
        print("{0:d} argument:".format(len(argv) - 1))
        for i in range(len(argv) - 1):
            print("{0:d}: {1}".format(i + 1, argv[i + 1]))
    elif len(argv) > 2:
        print("{0:d} arguments:".format(len(argv) - 1))
        for i in range(len(argv) - 1):
            print("{0:d}: {1}".format(i + 1, argv[i + 1]))
