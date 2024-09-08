# Write a program to detect double space in a string. 

def double_space_detector(str):
    if "  " in str:
        return True
    return False

str = input("enter the string : ")

if (double_space_detector(str)):
    print("Double space detected ")
else:
    print("No Double space detected")
