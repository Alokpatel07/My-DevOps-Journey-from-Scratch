import sys

# Using if-else
value = sys.argv[1]

if value == "t2.micro":
    print("Okay, we will create an instance..")
else:
    print("You are using free tier")


# Using If-elif-else
marks = int(sys.argv[2])
if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
else:
    print("Grade: D")



username = "Daenerys"
if len(username) > 0:
    print(f"Welcome {username}")
else:
    print("Enter valid username")


x = 19
if x > 10:
    if x < 20:
        print("X lies between 10 and 20")
