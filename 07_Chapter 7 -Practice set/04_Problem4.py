# Write a program to find whether a given number is prime or not.

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2 , int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

try :
    num = int(input("Enter the number : "))
    if is_prime(num) :
        print("Entered number is prime.")
    else:
        print("Entered number is not a prime number.")

except ValueError:
    print("Enter valid integer number.")