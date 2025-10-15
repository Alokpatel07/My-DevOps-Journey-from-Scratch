# Arithematic Operators

a, b = 10 , 5

print("Sum:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b) # Gives result in point
print("Floor Division:", a // b) # Gives result in integer
print("Modulus:", a % b) # Give remainder as result
print("Power:", a ** b) # Gives 10 to the power 5


# Assignment Operator

a = 10
a += 5  # Equivalent to a = a + 5
print(a)   # 15
a *= 2  #  Equivalent to a = a * 2
print(a)   # 30
a -= 5  #  Equivalent to a = a - 5
print(a)   # 25
a /= 2   # Equivalent to a = a / 2
print(a)   # 12.5
a //= 5  # Equivalent to a = a // 5
print(a)   # 2.0
a **= 2  # Equivalent to a = a ** 2
print(a)   # 4.0
a %= 4  # Equivalent to a = a % 4
print(a)   # 0.0

# Relational ( Comparison ) Operator

x = 5
y = 3
print(x == y) 
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

# Logical Operator

x = 5
print(x > 2 and x < 10)  # True
print(x > 10 or x == 5)  # True
print(not(x > 2))        # False

# Identity Operator

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)        # True (same object)
print(x is y)        # False (different objects)
print(x == y)        # True (same values)
print(x is not y)    # True

# Membership Operator

fruits = ["apple", "banana", "cherry"]
print("apple" in fruits)       # True
print("grape" not in fruits)   # True

num = [1, 3, 5, 8]
print(1 in num)  # True
print(7 in num)  # False
print(9 not in num)  # True