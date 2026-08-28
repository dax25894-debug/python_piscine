#!/usr/bin/env python

number_1 = int(input("Please enter the first number: "))
number_2 = int(input("Please enter the second number: "))

result = number_1 * number_2
print(number_1, "*", number_2, "=", number_1*number_2)

if result > 0:
    print("The result is positive.")
elif result < 0:
    print("the result is negative")
else:
    print("The result is positive and negative.")

