#!/usr/bin/env python

import sys


if len(sys.argv) > 2:
    for i in sys.argv[1::]:
        if "ism" not in i:
            print(i + "ism")
else:
    print("none")