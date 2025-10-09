# Variable in Python

x = 5      # integer variable
y = "alok"     # string variable
# type() function is used to know the data type of a variable
print(type(x))
print(type(y)) 

#Declaring string variables using single and double quotes
   
a = "Alok"
print(a)
a = 'Dev'
print(a)

#case sensitivity in variable names
a = 3
A = 4
print(a, A)  

#way to declare multiple variables of different data types in one line
x,y,z = 1, 2.5, "Alok"        
print(x)
print(y)            
print(z)

#Global variables and local variables

#A variable declared outside of a function is a global variable and can be accessed anywhere in the program.
#A variable declared inside a function is a local variable and can only be accessed within that function.

x ="awesome"   #global variable
def myfunc():
    x = "fantastic"  #local variable
    print("Python is", x)  #prints the local variable

myfunc()

print("Python is", x)  #prints the global variable


#Global keyword
#If we want to create a global variable inside a function, we can use the global keyword.
x ="Awesome"   #global variable
def myfunc():       
    global x       #declare x as a global variable
    x = "fantastic"  #change the value of the global variable
    print("Python is", x)  #prints the local variable
myfunc()
print("Python is", x)  #prints the changed value of the global variable
