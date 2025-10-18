print(10 > 9) 
print(10 == 9)
print(10 < 9)


# Prints message based on the condition
a = 100
b = 30
if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

# bool() function
# 1. For numbers
print(bool(4)) # If we don't pass any value to bool, it will return false
print(bool()) 

# 2. For strings
print(bool("Alok"))
print(bool("")) # For empty string , it will return false

# 3. For List
print(bool([1,2,3])) 
print(bool([]))  # This is empty list, returns false

# 4. For tuples
print(bool((2))) 
print(bool(())) # Empty tuple, returns false

# 5. For dictionary
print(bool({"name": "Alok"}))
print(bool({})) # Empty dictionary, returns false

# 4. For none
print(bool(None)) # For none , always returns false


a = [1,2]
if bool(a):
    print("a has value")
else:
    print("a is empty")

print(True + False) # true = 1 & false = 0
print(True + True + True)
print(False + False)