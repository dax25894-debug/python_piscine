#!/usr/bin/env python

user_input = 1
for i in range(11):
    print("Table of",i,":", end=" ")
    for j in range(11):
        print( i * j, end=" ")
    print()