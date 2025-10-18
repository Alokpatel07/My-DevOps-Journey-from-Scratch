#Strings can be written in both single quotes ('') and also with double quotes ("") 

a, b = 'Alok', "Abhay"
# print(a)
# print(b)

print("Hello", a)
print("Hi", b)

#Multiline Strings
x = """Hello All,
this is a,
Multiline string """
print(x)

#Strings as array

str = "Alok Patel"
for x in str:
    print(x)

print(len(str)) # len() function is used find the length of the string
print(str[0]) 

#Slicing in string
#Slicing is used to print the range of characters from a given string

b = "Hello World"
print(b[1:4]) # Prints char from index 1 to index 3 , index 4 char is not included
print(b[:5]) # From starting to index 5-1
print(b[2:])  # From index 2 to end of string
print(b[::-1]) # This is for reversed sequence
print(b[::2])  # Prints every second character
print(b[4:11:3]) # Prints every 3rd char from index 4 to 11-1 index

#Modify Strings

print(b.upper()) # Prints string in upper case
print(b.lower())  # Print string in lower case
print(b.strip())  # Remove whitespaces from string
print(b.replace("Hello", "Alok")) # Replaces Hello to Alok
print(b.split()) 
print(b.capitalize()) # Converts the first character to upper case


# Matchng Substring inside string
text = "Python is simple"
# print("Python" in text) # This will return in True or False
if "Python" in text:
    print('"Python" is found in text')
else:
    print("text not found")


# Concatenation
a = "Python"
b = "is"
c = "awesome"
result = a + " " + b + " " + c
print(result)

# f-string
age = 23
text = f"My name is Alok, my age is {age}"
print(text)

txt = f"Price of BMW is ${10000 * 1000} dollars"
print(txt)

# Escape character \
text = "We are \"Vikings\" from north." # by using escape char. we can use  double quote string inside a double quote string
print(text)