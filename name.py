#!/bin/python3
import sys
 
try:
    print("Hello my name is", sys.argv[1])

except IndexError:
    
    name = input ("What is your name since you forgot about it? ")
    
    print (f"Hello {name}")

