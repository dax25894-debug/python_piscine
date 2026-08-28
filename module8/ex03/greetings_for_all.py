#!/usr/bin/env python

def greetings(self = "noble stranger."):
    if isinstance(self,str):
        print("Hello,",self)
    else:
        print("Error! It was not a name.")

greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)