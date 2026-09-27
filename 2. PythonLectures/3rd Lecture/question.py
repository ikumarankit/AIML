info = [
    ("Alice", "Math"),
    ("Bob", "Science"),
    ("Alice", "Science"),
    ("Charlie", "Math"),
    ("Bob", "Math"),
    ("Alice", "English"),
    ("Charlie", "English")
]

# Ques:- Given a list of tuples with info(name, subject):
# .list all unique Course
for tup in info:
    print(tup[1])

for name, course in info:
    print(name, course)


unique_courses = set()

for val in info:
    unique_courses.add(val[1])
    
print(unique_courses)


# .list students enrolled in english
for name, course in info:
    if course == "English":
        print(name)


# .create dictinory (student name : set of courses)

student_dictinory = {}

for name, course in info: 
    if(student_dictinory.get(name) == None):
        student_dictinory.update({name: set()})

    student_dictinory[name].add(course)

print(student_dictinory)








