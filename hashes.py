def reverse(list):
    reversed = []
    for i in range(len(list),0,-1):
        
        reversed.append(i)

    return reversed 
print(reverse([1,2,3,4]))
