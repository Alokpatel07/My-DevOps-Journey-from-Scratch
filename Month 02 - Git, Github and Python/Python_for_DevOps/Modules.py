# Python Modules 
# Module is simply a python file that contains functions, variables, classes and other modules also via import 

import Function as basic_calc  # as is used as alias
# from function import addition
print(basic_calc.addition(8,9))

# random module
import random
print(random.randint(1,8))

# datetime module
import datetime
x = datetime.datetime.now()  # prints date and time
print(x)

# os module
import os
print(os.name)  # system name 
print(os.getcwd())   # prints curren working directory(cwd)