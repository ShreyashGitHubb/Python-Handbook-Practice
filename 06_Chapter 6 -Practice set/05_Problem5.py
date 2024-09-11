#  Write a program which finds out whether a given name is present in a list or not. 

list = ["leo","max","ivy","zoe","sam"]

name = input("enter the number : ")

name = name.lower()

if (name in list) : 
    print("name is persent in the list")

else:
    print("name is not present in the list")
