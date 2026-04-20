from check_grade import check_grade
from check_grade import check_name

students = {}

print("\n===================GRADE SYSTEM==================\n")
while True:  #loop for number of students you wanna key in 
    try:
        student_number = int (input("How many students:(numbers only) "))
        break

    except ValueError:  #incase you enter a non-integer
        print ("You have not entered a number!!")


for i in range (student_number):
        while True: #To keep the user in the loop until they key in the correct name no numbers or special characters 
            name = input (f"Enter student {i+1}'s name: ").title ()

            if check_name(name) == True:
                break

            else:
                print (check_name(name))
                continue
      
        while True:   # keeps user in loop until they enter the correct grade no numbers or special characters
            
            grade = input (f"Enter student {i+1}'s grade: ").upper()

            if check_grade(grade) == True:
                break
            else:
                print (check_grade(name))
                continue
        students [name]= grade
     
print ("\n===================RESULTS======================")
print ("=====NAME==============================GRADE====")

for b,student in enumerate(students,start=1): # I looked up enumerate function though
   
    print (f"{b}.",student,"\t\t",students[student],)
    