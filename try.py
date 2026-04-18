#!/bin/python3

while True:
    
    try: # so if the try encounters an error the int func raises a ValueError
        
        x= int(input("what's your number: "))
   
    
    except ValueError:  # so this handles the valueError right 
        
        print("x is not an integer")

    
    else: # So this evaluates only when the try succeeds
    
        print (f"x is {x}")
        break
    
    
     # I think u now understand how try except and else works