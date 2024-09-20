# Write a program to find the sum of first n natural numbers using while loop. 

def sum_of_natural_num(n):
    sum = 0
    count = 1
    while count <= n:
        sum = sum + count
        count = count + 1 
    return sum

n = int(input("Enter natural number n : "))
result = sum_of_natural_num(n)
print(f"The sum of the first {n} natural numbers is: {result}")