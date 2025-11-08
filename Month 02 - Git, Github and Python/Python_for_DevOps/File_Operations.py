import os

f= open("file.txt")
print(f.read())
f.close()

#   OR using with statement 
with open("file.txt") as f:
    print(f.read())

# Note : if we are opening file using with , we do not need to close the file, with statement takes care of it

with open("file.txt") as f:
    print(f.read(5)) # This prints specified no of characters

# For one line use readline() method
with open("file.txt") as f:
    print(f.readline())

# readlines() method ---> Reads all lines from a file and return a list of strings 
with open("file.txt") as f:
    print(f.readlines())

# Using for loop to read lines of file
with open("file.txt") as f:
    for x in f:
        print(x)

# Write in file

# using append method
with open("file.txt", "a") as f:
    f.write("\nNew Line added to the files")

# open and read the file after the overwriting:
with open("file.txt") as f:
    print(f.read())

# using write method --->  the "w" method will overwrite the entire file.
with open("file.txt", "w") as f:
    f.write("New content added, prev was updated")
with open("file.txt") as f:
    print(f.read())

# Create a new file
with open("newfilee.txt", "x") as f:
    pass

# Deleting a file
os.remove("newfilee.txt")
# os.rmdir("myfolder")  ----> used to remove empty folders