with open("students.csv") as read:
    for line in read:
        Line = line.rstrip().split(",") # python is case sensitive remember hehe
        print (f"{Line[0]}is in {Line[1]}")

'''
rstrip() removes the newline from every line ending and 

split() splits the lines from the separator you want like comma and shii like that

'''