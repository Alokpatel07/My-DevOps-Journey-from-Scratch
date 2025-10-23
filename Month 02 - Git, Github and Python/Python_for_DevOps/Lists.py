# List

# creating list
fruits = ["Apple", "Cherry", "Orange"]
print(len(fruits))  # prints the length of the list items
print(len(fruits[0]))   # prints the length of first element or 0th index no. element from the list

list_random_data_type = [1, 8, "alok", 0.4, "Abhay"]
print(list_random_data_type)

# Creating list using list() constructor

thelist = list(("BMW", "Audi", "Lambo", "Ferrari"))
print(thelist)


# Accessing list items using index number

name = ["Alok", "Abhishek", "Shivam", "Akshat", "Abhay"]
print(name[0])  # prints the 0th index number element
print(name[0:3])  # prints name as string indexing concept
print(name[::-1])  # reverses the list
 
cars = ["BMW", "Audi", "Mercedes", "Bentley", "Bugatti", "Lambo", "Ferrari"]
print(cars[-4:-1])  # negative indexing

# checking if element exist in list

if "BMW" in cars:
    print("This is most luxurious car you have ...")

# CHANGE LIST ITEMS

# change specific item
cars[1] = "Cadillac"
print(cars)

# change range of item values
cars[0:3] = ["Cadillac", "Supra", "Aston Martin"] 
print(cars)

# Insert new Items  (we can insert new item at specific index provided by us)
cars.insert(0, "BMW") # inserts item at index 0
print(cars)

# append items (add an item at the end of the list)

cars.append("Dodge Challenger")
print(cars)

# Extend List ---> add elements from another list at  the end of an existing list
indian_car = ["Maruti", "Mahindra", "Thar"]
cars.extend(indian_car)
print(cars)

# we can add any iterable object like tuples, sets, dictionaries to an existing list
more_cars = ("Range Rover", "Defender", "Toyota")
cars.extend(more_cars)
print(cars)


# Remove List Items
cars.remove("Toyota")
print(cars)

# Sorting the list numbers
number = [3,0,9,8,2]
number.sort()
print(number)

# Concatenate two particular values from the list
print(cars[0] + " " + cars[4])