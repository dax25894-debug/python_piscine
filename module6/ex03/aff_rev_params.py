#!/usr/bin/env python

import sys

x = sys.argv[1:]
if len(x) > 2:
    for i in x[::-1]:
        print(i)
else:
    print("none")