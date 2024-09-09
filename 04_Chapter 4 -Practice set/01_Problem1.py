#  Write a program to store seven fruits in a list entered by the user. 

fruits = [] # empty list

for i in range(7):
    fruit = input(f"Enter the name of the fruit {i+1} : ")
    fruits.append(fruit) # append the name of the fruits into the list

# printing the entered fruits
print("you have enter the name of the fruits are :- ")
print(fruits)