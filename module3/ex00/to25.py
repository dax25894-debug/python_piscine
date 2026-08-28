#!/usr/bin/env python

user_input = int(input("Enter a number less than 25 : "))
if user_input in range(1,26):
    for i in range(user_input,26):
    
        print("Inside the loop, my variable is ", i)
else:
    print("Error")
