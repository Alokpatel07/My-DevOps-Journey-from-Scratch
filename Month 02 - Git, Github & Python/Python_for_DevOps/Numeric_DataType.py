# Different numeric data types in Python

x = 1
y = 2.5
z = 1 + 2j
print(type(x))
print(type(y))
print(type(z))

#Type conversion in Python

x = 1    #int
y = 2.8  #float
z = 1j   #complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

#convert float to complex:
d = complex(y)

print(a)
print(b)        
print(c)
print(d)

print(type(a))
print(type(b))
print(type(c))
print(type(d))