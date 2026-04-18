def main():
   number = get_number()
   meow(number)


def meow(n):
    if isinstance(n,int): # I used the isinstance () function 
      
       for i in range (n):
         print (f"{i+1}. Meow!!")
         
    else:
        print ("You entered zero nigga!!")

def get_number():
   number = int (input("Enter number of times you want me to meow: "))
   if number>0:
        return number
   else :
        return "Number must be more than 0 dummy"

main()

# you can get the notes on isintance in your obsidian