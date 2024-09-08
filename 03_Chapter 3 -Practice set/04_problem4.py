# Replace the double space from problem 3 with single spaces.

def double_space_detector(str):
    if "  " in str:
        return True
    return False

def replace_double_space(str):
    return str.replace('  ',' ')

str = input("enter the string : ")

if (double_space_detector(str)):
    newstr = replace_double_space(str)
    print("original string :",str)
    print("corrected string :",newstr)
else:
    print("No Double space detected")
    print("string is correct")