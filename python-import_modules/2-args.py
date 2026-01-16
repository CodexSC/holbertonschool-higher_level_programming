#!/usr/bin/python3
from sys import argv
"""
Prints the number of and list of arguments."""
if __name__ == "__main__":
    count = len(argv) - 1

    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
    else:
        print(f"{count} arguments:")

    for i in range(1, count + 1):
        print(f"{i}: {argv[i]}")
