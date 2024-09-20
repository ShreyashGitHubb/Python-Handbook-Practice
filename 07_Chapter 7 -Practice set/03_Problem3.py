# Attempt problem 1 using while loop.

def multiplication_Table(number):
    print(f"Multiplication tabel of {number}")
    i = 1
    while i <= 10:
        print(f"{number} X {i} = {number*i}")
        i += 1 
try:
    num = int(input("Enter the number to get the multiplication table : "))
    multiplication_Table(num)
    
except ValueError:
    print("Please enter a valid integer.")