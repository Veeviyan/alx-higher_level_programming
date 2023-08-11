#!/usr/bin/python3
# File name: 2-args.py
# Auth: Vivian Okaforcha

import sys

if __name__ == "__main__":
    def main():
        no_of_args = len(sys.argv) - 1
        print(f"{no_of_args} argument(s):")

        for i, arg in enumerate(sys.argv[1:], start=1):
            print(f"Argument {i}: {arg}")
