#!/usr/bin/python3
import sys

argv = sys.argv
i = 1

while i < len(argv):
    arg = argv[i]
    print(arg, end=" ")
    i += 1

print()
print("{}-args.py {}".format(argv[0], ' '.join(argv[1:])))
print("{} arguments:".format(len(argv) - 1))
i = 1
while i < len(argv):
    print("{}: {}".format(i, argv[i]))
    i += 1
