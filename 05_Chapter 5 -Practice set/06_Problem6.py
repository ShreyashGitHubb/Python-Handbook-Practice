# Create an empty dictionary. Allow 4 friends to enter their favorite language as 
# value and use key as their names. Assume that the names are unique. 

dict = {}

name = input("enter friend name : ")
lang = input("enter the language name : ")
dict.update({name : lang})

name = input("enter friend name : ")
lang = input("enter the language name : ")
dict.update({name : lang})

name = input("enter friend name : ")
lang = input("enter the language name : ")
dict.update({name : lang})

name = input("enter friend name : ")
lang = input("enter the language name : ")
dict.update({name : lang})

print(dict)