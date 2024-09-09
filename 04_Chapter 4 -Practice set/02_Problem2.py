#  Write a program to accept marks of 6 students and display them in a sorted manner.

Marks = []

for i in range(6):
    while True :
        try:
            Mark = float(input(f"Enter the marks of student {i+1} : "))
            if 0<= Mark <= 100 :
                Marks.append(Mark)
                break
            else:
                print("Mark shoud betweem 0 to 100, please enter again")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
        
Marks.sort()

print("Marks in shorted order")
print(Marks)