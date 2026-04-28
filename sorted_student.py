students = []

with open ("students.csv") as file:
    
    for lines in file:
        
        name,house = lines.rstrip().split(',')

        student= {"name":name,"house":house}

        students.append(student)

def get_house (students):
    return students["house"]

def get_name (students):
    return students["name"]


for anything in sorted (students, key=get_name):
    print (f"{anything['name']} is in {anything['house']}") #yeah really glad you fixed this bug to be honest
#print (sorted (students, key=get_name))
#print(student)