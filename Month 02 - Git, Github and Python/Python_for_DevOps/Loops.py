# For Loop

for i in range(1,11):
    print(i)

# Loop through Lists
fruits = ["apple", "banana", "cherry"]
# for x in fruits[0]:  this will iterarte through first element from the list
for x in fruits:
    print(x)

# Loop through Strings
name = "Alok"
for i in name:
    print(i)

# Loop through with range(start, stop, step)
for i in range(2,11,2):
    print(i)

# Break statement
for i in fruits:
    print(i)
    if i == "banana":
        break

# While Loop
i = 1
while i <= 5:
    print(i)
    i += 1

# Infinite Loop
# while True:
#     print("Hello World")

# While loop with break
i = 1
while i < 6:
    if i == 4:
        break
    print(i)
    i += 1

# Continue statement
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)