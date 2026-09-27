# String in Python -: Strings can be defined in single, double, triple quotes
word = "python"
print(len(word))   # len function is used for any sequence like list, string, tuple, dictnory

# Indexing -: start from 0          
print(word[2])

# traversing 
for ch in word:
    print(ch)

# Immutability -: cannot changes or modify the string 
# word[2] = 'f'  # gives error 



# Operations we can performed on strings 

# concatenate 
word1 = "I love"
word2 = "python"
sentence = word1 + " " + word2
print(sentence)


# Slicing 
# we can slice a string and create sub string 
str = "Python i study"

# str[start index (default value is 0): end index(exclusive)(optional) (default value is string length)]
print(str[2:4])
print(str[2:])
print(str[:])

# we can also use negative index to slice a string 
print(str[-4:-2])





# String Formatting -: when we want to create dynamic string(string in which we can use different values and variables like sum is 25)

# 1st Way of formatting string: using format() function 
# introduce in python3 
# we use placeholder{} and placement value 
a = 5 
b = 10
sum = a + b

# normal formatting 
print("Language is {}".format("python"))
print("Sum is {}".format(sum))
print("Sum of {} and {} is {}".format(a, b, sum))

# index based formatting 
print("Sum of {1} and {0} is {2}".format(a, b, sum))

# value based formatting  -: we can create variables inside the format function itself 
print("values{a}{b} of vars {a} & {b}". format(a=5, b=10))

                            
# 2nd Way is F-string
# introduce in version 3.6
# we use Literal string interpolation in F-string in python
print(f"sum of {a} & {b} is {a + b}")
print(f"avg of {a} & {b} is {(a + b) / 2}")






# Four Important built-in data types or classes of python: 
# 1.List   2.Tuple  3.Dictnories and 4.Sets 


# 1. List 
# mutable sequence of values 
# marks1 = 99
# marks2 = 89
# marks3 = 65
# marks4 = 92
# marks5 = 100

# instead of creating multiple variables to store same type of information we can use list 
marks = [99, 89, 65, 92, 100]   
print(marks)
print(marks[1])
# print(marks[6])  # gives error invalid index 
print(len(marks))

# string are immutable but lists are mutable 
marks[2] = 85
print(marks)

print(type(marks))
# we can also store diffrent types of data in list 

list = [12, 13, 14, 15, 16, "abc", "def", 10.99]
print(type(list))                               


# slicing 
# we can also perform slicing operation on list 
# string -> slicing -> creates substring 
# list -> slicing -> creates sub list 

# list[start index (default value is 0): end index(exclusive)(optional) (default value is list length)]

print(list[0:5])
print(list[:5])
print(list[5:])
print(list[:])

# we can also use negative index to slice a list 
print(list[-5:-2])
print(list[-5:])



# we can use multiple methods or functions on list 
# methods are classes functions like list are classes and the function we write for it is called methods 

# 1. list.append(val) :- add one element at the end 
nums = [1, 2, 3]

nums.append(4)
print(nums)

# 2. list.insert(idx, val)  :- insert element at any given index 
nums.insert(2, 10)
print(nums)

# 3. list.sort()  :- arranges in increasing order 
nums.sort()
nums.sort(reverse=True)   # for decreasing order sorting
print(nums)

# 4. list.reverse()  :- reverses order 
nums.reverse()
print(nums)



# Loops with list 
# because list is sequencial data set that is why we can use for loop 

for val in nums:
    print(val)


# Quess:- Search an index for a given number n in list
n = int(input("Enter number: "))
idx = 0

for val in nums:
    if(val == n):
        print(f"Exists on index {idx}")
        break

    idx += 1