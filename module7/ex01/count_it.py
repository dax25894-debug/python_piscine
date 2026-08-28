#!/usr/bin/env python

import sys
parameters = len(sys.argv) - 1
x = sys.argv
if parameters > 0:
    for i in x[1:]:
        print(i, ":", len(i))
else:
    print("nope")