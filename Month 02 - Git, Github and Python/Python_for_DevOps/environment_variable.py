import os


# List all environment variable
# for key, value in os.environ.items():
#     print(f"{key} = {value}")



# How to Set Environment Variables

""" 1. On Windows (Command Prompt) 
       set MY_NAME="Alok" """

""" 2. On Windows (Power Shell)
       $env:MY_NAME="Alok" """

""" 3. On Linux/Mac
       export MY_NAME="Alok" """

# This command prints name which I have given to variable

print(os.getenv("My_passwd"))