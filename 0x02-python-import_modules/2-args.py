#!/usr/bin/python3
# File name: 2-args.py
# Auth: Vivian Okaforcha

from sys import argv

if __name__ == "__main__":
    n = len(argv) - 1
    str = "arguments"

    if n == 0:
        print("0 arguments.")
    elif n == 1:
        print("1 argument:")
    else:
        print("{} {}:".format(n, str))

    for i in range(n):
        print("{}: {}".format(i + 1, argv[i + 1]))
