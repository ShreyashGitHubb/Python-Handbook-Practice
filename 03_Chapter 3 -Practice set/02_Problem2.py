# Write a program to fill in a letter template given below with name and date. 
#   letter = '''  
#   Dear <|Name|>, 
#   You are selected! 
#   <|Date|> 
#   ''' 

letter = '''  
    Dear <|Name|>, 
    You are selected! 
    <|Date|> 
''' 

def fill_letter (name , date):
    filled_letter = letter.replace('<|Name|>',name).replace('<|Date|>',date)
    return filled_letter

name = input("enter the name : ")
date = input("enter the date : ")

print(fill_letter(name,date))