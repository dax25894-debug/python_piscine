#!/usr/bin/env python

import sys


def enlarge(self):
    while len(self) < 8:
        self += "z"
    return self

def shrink(self):
    if len(self) < 8:
        return enlarge(self)
    elif len(self) > 8:
        return self[:8]
    else:
        return self

for self in sys.argv[1:]:
    print(shrink(self))