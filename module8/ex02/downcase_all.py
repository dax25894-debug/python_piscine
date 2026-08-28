#!/usr/bin/env python

import sys

def downcase_it(text):
    return text.lower()


params = sys.argv[1:]

if len(params) == 0:
    print("none")
else:
    for word in params:
        print(downcase_it(word))

