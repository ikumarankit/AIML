print("Hello World")
print("Hello World", "with Python")
print("Hello\nWorld", "with Python")

# Variables
# Variables or function names in python called Identifiers 
name = "Ankit"
age = 35
PI = 3.14

print(name)
print(name, age, PI)
print("My name is: ", name)
print("My age is: ", age - 1)


# Indentation 
# structing lines or codes in python 
# python is case sensitive language 
# Identifiers does not start with number but can start with _, alphabet(including lowercase and uppercase)



# Data Types
# .Integer
# .String
# .Float
# .Boolean 
# .None 

print(type(age))
print(type(name))    # str -> String (', "", ''')
print(type(1.22))

# Boolean
# True or False 

num = 2
isPrime = True
print(type(isPrime))


# None 
# jis bhi variable ko ham value assign nahi karna chahte usko ham none assign kar dete hai 


# Keywords in python 
# reserved words meaning is fixed we cannot use it as identifiers name 

# Comments -> is used to help other developer or programmers understand the code by telling him/her what our code or program do

# multiline comments -> ''' Hello this is multi line comment '''



# Style Guide -> chijo ko likhne ka tarika
# -> we use snake case to write python program -> tot_price = 999.99, full_name = "Ankit Kumar "


# WAP to sum two numbers 
a = 10
b = 5
sum = a + b
print(sum)



# Operators  
# .Arithmetic->   +, -, *, /, %, **
print(a + b)
print(a - b)
print(a * b)
print(a / b)   # 2.0
print(a % b)   # calculate remainder 
print(a ** b)  # a to the power b

# .Relational/Comparison->   >, >=, <, <=, ==, !=  return either True or False value
print(a < b)
print(a > b)
print(a == b)
print(a != b)

# .Assignment->    =, +=, -=, *=, /=, %=
a = a + 1
a += 1
print(a)

# .Logical-> and, or, not
# not-> makes True value false and vice versa 
var = False
print(not var)  #True
print(not (5 > 8))   # True 

# and-> if both true then only returns true
# we use not with single expression but we use add with more than two expression
print((5 > 1) and (5 > 0))  # True
print((5 > 1) and (5 < 0))  # False

#or-> return True if any one of the expression is True, return True if both True also and return False only when all expression is False
print((5 < 1) or (5 < 0))  # False
print((5 > 1) or (5 < 0))  # True


# There is also Bitwise operator or membership operator in python 


# Ques
x = 3
x += 5
print(x)   #8


# Operator Precedence and associativity 
# Operator precendence determines which operator to be executed first and operator associativity determines the direction of execution if operator share the same precendence 
# . ()
# . **  (power)  (in power case if there is multiple expression then the execution will happens in right to left)
# . *,/,%    (left to right associativity)
# . +,-
# . ==, !=, >, >=, <, <=
# . not
# . and
# . or 

# we solve expression with the help of operator precendence and associativity rule 



# Type Conversion -> converting one type of data into another 
# only possible in compatible datatypes like int -> float, float -> int, int -> boolean   not "abcd" -> int but we can convert "123" -> int 123
print(a / 5)
print(1.22 + 5)
print(type(a / 5))

# Type conversion is of two type 
# 1. Type conversion (Implicit conversion in java widening conversion)
# like float + int gives float value because we dont want to lose data 

# 2. Type Casting (explicit type conversion -> developer manually do, possible only in compatible datatype) 
print(int(a / 5))
print(int(1.22 + 5))


# so
ans1 = int(5 + 10.0)  #casting 
ans2 = 5 + 10.0  #conversion

print(ans1, type(ans1))
print(ans2, type(ans2))

# we can also typecast integer value into boolean value 
print(type(int("123")))
print(type(bool(10)))    # False -> 0 and True is every non zero value




# User Input -> we use input() to take input from any user

d = input("enter value of d: ")
print(d)

username = input("enter your username: ")
print("welcome", username)


# whatever value we take input using input() is the string value so we need to typecast the input data to get the correct result 
num5 = int(input("enter num5: "))
num6 = int(input("enter num6: "))
sum7 = num5 + num6   # String + String  this operation is called concatination
print(sum7)



# WAP to print the average of 2 numbers 
x1 = float(input("Enter 1st number: "))
x2 = float(input("Enter 2nd number: "))
avg = (x1 + x2) / 2
print(avg)
