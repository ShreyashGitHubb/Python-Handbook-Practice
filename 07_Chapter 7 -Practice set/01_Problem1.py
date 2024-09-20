# Write a program to print multiplication table of a given number using for loop. 

def multiplication_Table(number):
    print(f"Multiplication tabel of {number}")
    for i in range(1,11):
        print(f"{number} X {i} = {number*i}")

try:
    num = int(input("Enter the number to get the multiplication table : "))
    multiplication_Table(num)
    
except ValueError:
    print("Please enter a valid integer.")