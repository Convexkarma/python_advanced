from function import get_square

def main ():
    print ("The squares of 4 and 5 are:",get_square(4) ,"and", get_square(5))
    test_square()

    
def test_square():
    assert get_square (4) == 16 # I used the new assert word that I've learnt , lemme see what it does
   
    if get_square (5) != 25:
        print ("Not equal to 25")

if __name__ == "__main__": # to prevent main() function being called when importing this file

    main()


# error printed is an AssertionError
'''
Traceback (most recent call last):
  File "/home/manu/Desktop/python_advanced/assert.py", line 14, in <module>
    main()
    ~~~~^^
  File "/home/manu/Desktop/python_advanced/assert.py", line 5, in main
    test_square()
    ~~~~~~~~~~~^^
  File "/home/manu/Desktop/python_advanced/assert.py", line 9, in test_square
    assert get_square (4) == 16 # I used the new assert word that I've learnt , lemme see what it does
           ^^^^^^^^^^^^^^^^^^^^
AssertionError
'''

