# LOOPS 
# 1. While loop 
# finite loop 

# Iterator variable names can be anything 
count = 1
while(count <= 5):
    print("Hello")
    count += 1

print("After loop count value is: ", count)   #6

# Infinite looop 
# while(True):
#     print("Hello")

# Ques 
# Print number from 1 to 5 using while loop
# Print number in reverse using while loop 
# Print multiplication table of any number 'n'

num = int(input("Enter number: "))

count = 1
while(count <= 10):
    print(num * count)
    count += 1


# Two important keywords : 
# 1. break -> To terminate a loop 
# Ques
# Print number 1 to 10 but stop when i is multiple of 6

# 2. continue -> To skip current iteration 
# Ques 
# Print number 1 to 10 but skip when i is multiple of 3

# Ques 
# Print all odd numbers from 1 to 10 




# 2. For loop -> we used for loop for sequential traversal
# for more practical use we use for loop 
string = "Hello"

# in -> membership operator is used to check presence of value of any sequence (sequence can list, tuple, dictnory, string etc)
for var in string:
    print(var)

# we can also use membership operator in conditional statement so this is how membership operator is used to check presence of any value
if 'o' in string:
    print("o exist in string")

# for loop for sequence of numbers 
# range(n) => 0 to n - 1
for i in range(5):    # 0 to 5 -1 is the range
    print(i)



# Ques: count how many 'i' in the word 
word = "artificial intelligence"
count = 0
for ch in word:
    if(ch == 'i'):
        count +=1

print("Count of i is: ", count)


# Ques 
# Print vowel count of a given string 
word = "artificial"
count = 0

for ch in word: 
    if ch in ('a', 'e', 'i', 'o', 'u'):
        count += 1

print("Count of vowel is: ", count)


# range function 
# range(start, stop, step)  -> generate number sequence start and step parameter is optional by default is 0 and +1 and the stop condition is exclusive 

for i in range(5):
    print(i)

for i in range(1, 6):
    print(i)

for i in range(1, 10, 2):    # odd numbers
    print(i)

for i in range(2, 11, 2):
    print(i)


# Ques 
# Print sum of first 'n' natural numbers.
n = int(input("Enter number: "))
sum = 0
for i in range(n + 1):
    sum += i

print(sum)