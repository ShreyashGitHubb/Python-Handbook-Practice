# A spam comment is defined as a text containing following keywords:   
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program to detect these spams. 

c1 = "Make a lot of money"
c2 = "buy now"
c3 = "subscribe this"
c4 = "click this"

message = input("enter your comment : ")

if (c1 in message) or (c2 in message) or (c3 in message) or (c4 in message) :
    print("this comment is spam")
else :
    print("this comment is not a spam")