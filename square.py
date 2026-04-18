def main ():
   
   n = int(input ('What side square do you want me to draw: '))
   print_square(n)


def print_square (sides):
    for i in range(sides):
        print ("*" * sides , sep = "")

main ()
