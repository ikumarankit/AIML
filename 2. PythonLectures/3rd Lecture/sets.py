# Sets:- collection of unique elements 
# elements in set must be of immutable type like string, tuple 
# sets itself can be mutable but the elements inside must be immutable 
# unordered 

s = {1, 2, 2, 3}

print(s)
print(type(s))
print(len(s))  # 3


# Empty set 
empty_set = {}  
print(type(empty_set))  # it does not create an empty set it create an empty dictionary

empty_set2 = set()  # this creates an empty set 
print(type(empty_set2))



# Sets methods 
# s.add(val)  # adds a val 
s.add(5)
print(s)

# s.remove(val)  # removes a val
s.remove(1)
print(s)

# s.clear()  # emptiess the set 
s.clear()
print(s) # set()

# s.pop()  # removes a randomm val 
s.add(1)
s.add(2)
s.add(3)
print(s)

s.pop()
print(s)

# s.union(set2)  # returns new union  (union means all uniques elements)
s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 8, 9, 10}         

print(s1.union(s2))

# s.intersection(set2)  # returns new intersection  (common elements)
print(s1.intersection(s2))




