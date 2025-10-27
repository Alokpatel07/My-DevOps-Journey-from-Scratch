# TUPLES

# Creating Tuple
fruits = ("Apple", "Mango", "Cherry", "Banana", "Kiwi", "Orange")
print(fruits)

# Single item tuple

tuples = ("Denver",) # Do not forget to add comma
print(type(tuple))

tuple1 = ("Denver")
print(type(tuple1)) # This is not a tuple , it tis considered as string

# Accessing tuple using indexing
print(fruits[2])
print(fruits[-1])  # negative indexing
print(fruits[2:5]) # range of indexing

# Checking if item exxist in tuple
if "Mango" in fruits:
    print("Yes, 'Mango' exist in fruits tuple")

# Changing tuple value (by converting them into list , change  value, and again convert them into tuple)
x = ("Alok", "Abhay", "Shivam", "Abhishek")
y = list(x) # This converts tuple into list
y[1] = "Akshat"  # Modifies list value
x = tuple(y)  # again convert list into tuple
print(x)

# Another example
cars = ("Bmw", "Audi", "Lambo", "Bentley")
new_cars = list(cars)
print(new_cars)
new_cars.append("Range Rover")
cars = tuple(new_cars)
print(cars)

# Deleting a tuple completely
thistuple = (1,2,4,5)
print(thistuple)
del thistuple

# Looping through tuple
name = ("alok", "shivam", "dev", "pankaj")
for x in name:
    print(x)

# Joining Tuple

num1 = (1,2,3)
num2 = (4,5,6)
result_tuple = num1 + num2
print(result_tuple)

# Nested Tuple
nested = ((1,2),(3,4,"Alok",1,1,1),(9,"Dev"))
print(nested[1][2])  


# Tuple Method
names = ("Alok", "Dev", "Abhay", "Alok", "Akshat", "Alok")
print(names.count("Alok"))  # count("") method prints the no of times a specified value occurs
print(names.index("Abhay"))   # prints the position or ( index no.) of first occurrence of a specified value