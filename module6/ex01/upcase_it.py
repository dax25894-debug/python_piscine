#!/usr/bin/env python

import sys

if len(sys.argv) == 2:
    for i in sys.argv[1:]:
        print(i.upper())
else:
    print("none")