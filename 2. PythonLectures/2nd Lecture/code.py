# Fundamental concept of python 
# 1. Conditional statements 
# . if 
age = int(input("Enter your age: "))

if age >= 18:
    print("You can vote")
    print("You can drive")

# . elif 
color = input("Enter color: ")

if color == "red": 
    print("STOP")
elif color == "yellow":
    print("READY TO GO")
elif color == "green": 
    print("GO")
else: 
    print("Wrong Color")


# . else 

if age >= 18:
    print("You can vote")
    print("You can drive")
else: 
    print("You can't vote")


# Ques
# IF age is below 13 print child, if between 13 and 18 print teenager and if above 18 print adult 

if(age < 13):
    print("Child")
elif(age > 13 and age <= 18):
    print("Teenager")
else: 
    print("Adult")


# Username and password using if else 
# Multiple of any number n or not using if else 
# the number is odd or even using if else 


# NESTING
username = input("Enter username: ")
password = input("Enter password: ")

if(username == "admin" and password == "pass"):
    print("Success")
else:
    if(username != "admin"):
        print("Wrong username")
    else:
        print("Wrong password")



# Match Case -> Alternative of if, elif and else statement 

days = int(input("Enter days number: "))

match days:
    case 1:
        print("MONDAY")
    case 2:
        print("TUESDAY")
    case 3:
        print("WEDNESDAY")
    case 4:
        print("THURSDAY")
    case 5:
        print("FRIDAY")
    case 6:
        print("SATURDAY")
    case 7:
        print("SUNDAY")
    case _: 
        print("Invalid input")






# LOOPS 
# 1. While loop 
# 2. For loop 