# Write a program to input eight numbers from the user and display all the unique numbers (once).
 
arr = set()

for i in range(8):
    arr.add(int(input(f"enter {i+1} number : ")))

print(arr)