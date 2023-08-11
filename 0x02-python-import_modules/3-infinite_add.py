#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":
    def main():
        n = len(argv)
        print(f"Total arguments passed:".format(n))

        print(f"\nName of script:".format(argv[0]))

        print(f"\nArguments passed:", end="")
        for i in range(1, n):
            print(argv[i], end="")

        Sum = 0
        for i in range(1, n):
            Sum = Sum + int(argv[i])

        print(f"\n\nResult:".format(Sum))
