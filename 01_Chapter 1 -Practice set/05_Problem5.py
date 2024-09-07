# Label the program written in problem 4 with comments.  

import os
# replace the path this '/' to the directory you want to list
path = '/'

# here os moduel use to list the contants in the directory using the listdir() function
contant = os.listdir(path)

# printing the list of directory  
print(contant)