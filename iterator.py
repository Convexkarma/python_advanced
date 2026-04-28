even_sum=0
odd_sum=0

for num in range (0,101):
    if num % 2 == 0:
        even_sum += num
    else:
        odd_sum += num

print (f"sum of odd numbers: {odd_sum} and sum of even numbers: {even_sum}")