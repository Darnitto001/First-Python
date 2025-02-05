
courses = ["MIT","Cyber Security","Data Science"]
print(courses)

#accesseng an element
print(courses[2])

#looping through an array
for a in courses:
    print("Course is",a)

#adding a new element into an array
courses.append("Laravel")
print(courses)

#Deleting an element from an array
courses.remove("Cyber Security")
print(courses)