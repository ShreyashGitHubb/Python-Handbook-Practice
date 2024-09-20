#  Write a program to calculate the factorial of a given number using for loop. 

def factorial (n):
    if n < 0:
        return "Factorial is not defined for negative number"
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2 , n+1):
            result = result * i
        return result

number = int(input("Enter the number to get the factorial : "))
print(f"The factorial of {number} is : {factorial(number)}")
