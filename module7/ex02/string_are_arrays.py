#!/usr/bin/env python

import sys

if len(sys.argv) < 2:
    print("none")
else:
    found = False
    for word in sys.argv[1].split():
        for i in word:
            if i == "z":
                print("z", end="")
                found = True
    if not found:
        print("none")
    else:
        print()