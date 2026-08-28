#!/usr/bin/env python

import sys

if len(sys.argv) == 2:
    x = input("What was the parameter? ")
    if x == sys.argv[1]:
        print("Good job!")
    else:
        print("Noop, sorry . . .")
else:
    print("none")
