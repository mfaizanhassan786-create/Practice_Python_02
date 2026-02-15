#Store following word meanings in a python dictionary :
# Like that : 
# table : "a piece of furniture with a flat top and one or more legs"
# cat : "a small animal"


mydict = {
    "table" : ["a piece of furniture", "lists of facts and figures"],
    "cat" : "a small animal"
}
print(mydict)

#You are given a list of subjects for students.
# Assume one classroom is required for 1 subject.
#How many classrooms are needed by all the students.

# "python", "java", "C++", "python" ,"JS"
#"java", "python", "java", "C++", "C"

subjects = {
    
"python", "java", "C++", "python" ,"JS"
"java", "python", "java", "C++", "C"
}
print(subjects)

# Write a program to enter marks of 3 subjects from the user
# and store them in a dictionary.
# Start with an empty dictionary & add one by one.
# Use subject name as key & marks as value.

marks = {}  # Start with an empty dictionary

# Adding subjects one by one
sub1 = input("Enter subject 1 name: ")
m1 = int(input(f"Enter marks for {sub1}: "))
marks[sub1] = m1  # Adding 1st subject

sub2 = input("Enter subject 2 name: ")
m2 = int(input(f"Enter marks for {sub2}: "))
marks[sub2] = m2  # Adding 2nd subject

sub3 = input("Enter subject 3 name: ")
m3 = int(input(f"Enter marks for {sub3}: "))
marks[sub3] = m3  # Adding 3rd subject

print("Marks dictionary:", marks)

# Figure out a way to store 9 & 9.0 as separate values in a set.

# Problem: In Python, 9 == 9.0 is True, so a set treats them as the same element.
my_set = {9, 9.0}
print("Normal set:", my_set)       # Output: {9}  — only one value is kept!

# Solution: Convert them to strings, which makes them distinct values.
my_set = {str(9), str(9.0)}
print("String set:", my_set)       # Output: {'9', '9.0'}  — both are stored!

