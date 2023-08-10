#!/usr/bin/python3
# 3-print_alphabt.py

# Vivian Okaforcha <snowygeenie@gmail.com>

for alphabet in range(97, 123):
    if alphabet not in range(101, 102) and alphabet not in range(113, 114):
        print("{}".format(chr(alphabet)), end="")
