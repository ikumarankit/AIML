# Tuples :- immutabel sequence of values 
# tuples can store different types of data

tup = (1, 2, 3, 4, 5, "abc", 3.14)
print(tup)
print(type(tup))
print(len(tup))
print(tup[2])

# tuple object does not support item assignment 
# tup[2] = 10  # gives error 

# single value list and tuple 
list = [1]
tup = (1)   # intrepreted as mathmatical expression
print(type(tup)) 

tup = (1, )  # this is valid single value tuple  
print(type(tup))


# slicing :- same slicing process
print(tup[0:3])
print(tup[:3])
print(tup[:])


# loop :- same looping process
for val in tup:
    print(val)


# Ques: Sum all the element of the tuple 
sum = 0
for val in tup:
    sum += val

print(f"sum of value is {sum}")




# Tuples Methods 
# tup.index(val)  # returns 1st occurence idx
# tup.count(val)  # counts total occurances

tup2 = (1, 2, 2, 3, 1, 2)
print(tup2.index(2))  # 1
print(tup2.count(2))  # 3