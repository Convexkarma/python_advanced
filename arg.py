#!/bin/python3
import sys

if len(sys.argv) < 2: # checks to see if number of arguments namely names is less than 2
	print ('Too few arguments')
	
elif len(sys.argv) > 2: # if more than one is going to print this in terminal
	print ('Too many arguments')
	
else:
    print ("Hello my name is",sys.argv[1])
# continue coding nigga
