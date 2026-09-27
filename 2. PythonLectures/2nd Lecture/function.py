# Functions -> reusabel piece of code

def hello():    #fucntion defination
    print("hello")
    print("from python")

hello()   #function call
hello()   #we can call multiple times 



# WAF that take two number a and b as parameter and return its sum 
def sum(a, b):   # a, b are parameters
    s = a + b
    return s

print(sum(2, 5))
print(sum(5, 5))


# WAF that take three number a, b, c and return its average


# in function first parameter is non-defualt parameter and the second parameter can be default parameter
def sum(a, b = 0):
    s = a+b
    return s

print(sum(3))



# Types of function in python: 
# 1. built-in function  like: print(), input(), type(), range()
# 2. user-defined function like we create sum function          



# Lamda Function -> small annonymous function that we defined using lambda keyword 

# lambda function defination 
# lambda parameter1, parameter2 : single_expression
# lambda function have multiple parameters but have only one expression

addition = lambda a, b: a + b
print(addition(2,2))

# lambda function is used for simple works and complex works 
# lambda function uses in high order function (high order function is a function in which the value we return is function or the parameter of that function is function)



# Ques 
# Factorial of any number n 

def calc_factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact * i

    return fact 

n = int(input("Enter number: "))
print(calc_factorial(n))