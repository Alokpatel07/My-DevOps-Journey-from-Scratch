x = "awesome" # x is global variable
def myfunc():
    # global x
    x = "fantastic" # x acts as local variable
    print("Python is", x)
myfunc()
print("Python is", x)

# Simple Calculator

num1 = 10
num2 = 5
def add():
    add = num1 + num2
    print("The addition is", add)

def sub():
    sub = num1 - num2
    print("The substraction is", sub)

def mul():
    mul = num1 * num2
    print("The multiplicaation is", mul)

add()
sub()
mul()

# Function with parameters
def greet(name):  # Here name is parameter which is variable inside a function
    print("Hello", name)

greet("Alok") # Here "Alok" , the actual value passed to function is called as argument


# Function with multiple parameters 
def sum(a,b):
    print(a + b)
sum(4,5)


# Example 2
def name(fname, lname):
    print("Hello",fname, lname)
name("Alok", "Patel")


# Function with return value
def sum(x,y):
    return x + y
# result = sum(8,9)
print("The sum of x and y is", sum(8,7))


# Function with by default parameter value
def greeting(name = "Alok"):
    print("Hello", name)
greeting() # This will return Hello Alok
greeting("Abhay")  # This will return Hello Abhay