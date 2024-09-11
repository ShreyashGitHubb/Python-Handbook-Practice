# Write a program to find out whether a student has passed or failed if it requires a 
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and 
# take marks as an input from the user.

sub1 = int(input("Enter the marks of subject 1: "))
sub2 = int(input("Enter the marks of subject 2: "))
sub3 = int(input("Enter the marks of subject 3: "))

if (((sub1 + sub2 + sub3) / 300) * 100 < 40):
    print("You have failed due to less percentage.")

elif (sub1 < 33 or sub2 < 33 or sub3 < 33):
    print("You have failed due to less marks in one or more subjects.")

else:
    print("You have passed!")
