def main ():
    n = int(input ("What number of side square do you want: "))
    print_square(n)

def print_square(n):
    for i in range (n): # The outer loop has to wait for the inner loop to finish to continue
        for j in range (n):
            print ("#", end = '') # You have to specify end because print in default ends with a newline
            
        print() # this is to print a new line after the inner loop is done 

         # if you put the print statement in the inner loop it will print a newline after every # symbol
    
main ()