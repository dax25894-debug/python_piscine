#!/usr/bin/env python

array = [2, 8, 9, 48, 8, 22, -12, 2]
new_list = []
print(array)
for i in array:
    if i >= 5:
        new_list.append(i + 2)
print(new_list)
