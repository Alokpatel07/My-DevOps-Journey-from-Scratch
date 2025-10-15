# Some simple example of sys module


import sys

name = sys.argv[1]
surname = sys.argv[2]
print("Hello,", name, surname)

num1 = int(sys.argv[3])
num2 = int(sys.argv[4])
sum = num1 + num2
mul = num1 * num2
# print("Sum:", sum)
print("Multiplication:", mul) 
print("Length of arguments:", len(sys.argv))

import os

# for key, value in os.environ.items():
#     print(f"{key} = {value}")

print(os.getenv("my_passwd"))