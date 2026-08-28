#!/usr/bin/env python

array = [2, 8, 9, 48, 8, 22, -12, 2]
new_list = set()
print(array)
for i in array:
    if array.count(i) == 1:
        new_list.add(i + 2)
print(new_list)
