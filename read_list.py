with open ("class_list.txt","r") as file: #r is not necessary because the default open reads  from a file
    lines = file.readlines()

for line in lines:
    print (f"Hello, {line}")
