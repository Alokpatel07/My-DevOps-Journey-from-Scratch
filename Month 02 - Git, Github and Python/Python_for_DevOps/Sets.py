# Sets are Immutable, Unordered, Unindexed and do not allow duplicate value

fruits = {"Apple", "Orange", "Mango"} 
print(fruits)  # The output does not have any specific order 
 
thisset = {"Apple", "Alok", True, False, 1, 2, 0}  # Here 1 and 0 are duplicate values of True and False 
print(thisset)
print(type(thisset))
print(len(thisset))

# We ca not use index no to access items in set , so we loop through sets
for x in thisset:
    print(x)

# Checking if value present in set or not

print("Alok" in thisset)

if "Appple" in thisset:
    print("Yes, 'Apple' is present in the set")
else:
    print("Apple is not present")

# Adding items in set
thisset.add("Marvel")
print(thisset)

# Add set item/value from another set
cars = {"Pagani", "BMW", "Mercedes"}
thisset.update(cars)
print(thisset)

# using .update() methos we can add any iterable object (tuples, list, dictionary)
games = ["BGMI", "COD", "Elden Rings"] 
thisset.update(games) # This adds a list values into an existing set
print(thisset)

# Removing items from set

# Using .remove() method
thisset.remove("Alok") # Removes Alok from the set and if the item we want to remove does not exist in set, this will cause an error
print(thisset)

# Using .discard() method
thisset.discard("Aman") # .discard() method does not raise an error if the item does not exist in set which we want to remove.
print(thisset)

x= thisset.pop() # Removes random item from the set
print(x)
print(thisset)

thisset.clear() # Empty the set
print(thisset)

# del keyword deletes the set completely
# del thisset
# print(thisset)

thisset.update(["Alok", "Abhay"]) # Add multiple value
print(thisset)

# Join sets using various ways

# Union 
set1 = {"a","b","c"}
set2 = {1,2,3}
set3 = set1.union(set2)
print(set3)

# OR using | operator
set3 = set1 | set2
print(set3)

x = {1,5,7}
y = ("Alok", "Abhay", "Akshat")
z = x.union(y) # Using union method we can join set with other data types like lists or tuples
print(z)

# Update
x = {"a","b","c"}
y = {1,2,3}
x.update(y)
print(x)

# Intersection (returns a new set)
set1 = {"Apple", "BMW", "Alok", "Abhay", "Audi", 1, 0}
set2 = {"Alok", "BMW", "Audi", "akshat", "Mercedes",True, False, 1}
set3 = set1.intersection(set2)
print(set3)

# OR using & operator
set3 = set1 & set2
print(set3)

# intersection_update() -----> method changes the original set instead of returning a new set
set1.intersection_update(set2)
print(set1)

# Difference
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
# set3 = set1.difference(set2)
set3 = set1.difference(set1) # Returns an empty set
print(set3)

#   OR using - operator
set3 = set1 - set2
print(set3)

# difference_update() --->  do not return a new set 
set1.difference_update(set2)
print(set1)

# Symmetric difference ----> return the items that are not present in both sets
setA = {"Iron man", "Spider-man", "Thor"}
setB = {"Batman", "Superman", "Iron man"}
setC = setA.symmetric_difference(setB)
print(setC)

# OR  using ^ operator
setC = setA ^ setB
print(setC)

# symmetric_differnce_update
setA = {"Ironman", "Spiderman", "Thor", "Thanos"}
setB = ("Batman", "Superman", "Ironman")
setA.symmetric_difference_update(setB)
print(setA)

# FROZENSET
# Creating a frozenset using frozenset() constructor
x = frozenset(("Alok", "Abhay", "Dev"))
print(x)
print(type(x))