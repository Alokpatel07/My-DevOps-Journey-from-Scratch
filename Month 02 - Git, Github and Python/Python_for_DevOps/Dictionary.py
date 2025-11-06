# Dictionaries are ordered, changeable, but do not allow duplicate value. These are written using {} "key": "value" pair inside these.

# Creating a Dictionary
thisdict1 = {
    "brand": "Ford",  # Dictionaries can not have two items with same key hence 
    "brand": "BMW",   # these are overwritten by latest value to the key
    "model": "Mustang",
    "year": 1964
}
print(thisdict1)
print(thisdict1["model"]) # using key as a reference

# The value in dictionary can be of any data type

thisdict = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "color": ["red", "blue", "black"]
}
print(thisdict)

# Accessing values
print(thisdict["brand"])

# Using .get() method
print(thisdict.get("year"))
print(thisdict.get("logo")) # If the key doesn't exixt , there will be no error in the output , you get None as output 

# Use .keys() and .values() method to print keys and value 
print(thisdict.keys())
print(thisdict.values())

print(thisdict.items()) # Return each item in a dictionary as tuples in list

# Checking if the exits in the dictionary
if "brandd" in thisdict:
    print("Yes, 'brand' is one of the key in thisdict")
else:
    print("The key does not exist in thisdict.")

# Change Values
cars = {
    "company" : "BMW",
    "models" : "M5",
    "year" : 2024
}
print(cars)
cars["models"] = "M4 Comp"
print(cars)

# Update Values
cars.update({"company" : "Audi"})
print(cars)
 
# Adding items using change and update value method
cars["color"] = "Z-Black"
print(cars)

cars.update({"engine" : "V16"})
print(cars)

# Remove Items
#  .pop("key name") method
cars.pop("year")
print(cars)

# .popitem() method removes items using the key which is last inserted
cars.popitem()
print(cars)

# del keyword for deleting specific key : value or deleting entire dictionary
del cars["color"] # removes specific key
print(cars)

# del cars  # deletes the entire dictionary
# print(cars)

# .clear() method removes the dictionary keys and values, not the entire dictionary
cars.clear()
print(cars)

# Looping through Dictionary
games = {
    "name" : "PUBG",
    "region" : "Global",
    "version" : 19,
    "year" : 2022
}
# For printing keys
# for x in games:
#     print(x)

for x in games.keys():
    print(x)

# For values
for x in games.values():
    print(x)

# For looping through keys and values at the same time, we can use items() method
for x, y in games.items():
    print(x,":",y)

# Copy a dictionary
my_games = games.copy()
print(my_games)

# Nested Dictionary
myfamily = {
    "child1" : {
        "name" : "Steve",
        "age" : 29
    },
    "child2" : {
        "name" : "Tom",
        "age" : 25
    },
    "child3" : {
        "name" : "kane",
        "age" : 19
    }
}
print(myfamily)
print(myfamily["child1"]["name"])

# Another example
person = {
    "name" : "Alok",
    "age" : 21,
    "skills" : ["Python", "AWS", "DevOps"]
}
print(person["skills"][1])