#!/usr/bin/env python

import sys
if len(sys.argv) < 3:
    print("none")
else:
    x = int(sys.argv[1])
    y = int(sys.argv[2])
    z = range(x,y + 1)

    if len(sys.argv) == 3 and sys.argv[1] < sys.argv[2]:

        for i in z:
            print(i)
    else:
        print("none")