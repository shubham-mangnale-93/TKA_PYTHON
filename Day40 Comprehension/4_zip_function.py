# zip:-------->>>
# it is used to combine multiple iterable.
"""
- zip() combines multiple iterables (lists, tuples, etc.) element-wise
  into pairs (or tuples), so you can loop through them together.
- Useful when you have two or more related sequences and want to
  process them side by side.
 
SYNTAX:
    zip(iterable1, iterable2, ...)
 
    You can pass 2 or more iterables. It pairs up items at the
    same index from each iterable.
"""
students = ["om","ganesh","ram","arun"]
marks = [55,66,77,88]
z_obj = zip(students,marks)
result = list(z_obj)
print(result)

students = ["om","ganesh","ram","arun"]
marks = [55,66,77,88]
for name,mk in zip(students,marks):
    print(f"{name} : {mk}")

#------------------------------------------------------------------------------------------------------

names = ['Amit', 'Priya', 'Rahul']
marks = [85, 90, 78]
 
print("Basic zip:")
for name, mark in zip(names, marks):
    print(name, mark)

cities = ['Pune', 'Mumbai', 'Delhi']
 
print("\nZipping 3 lists together:")
for name, mark, city in zip(names, marks, cities):
    print(name, mark, city)
 
# Expected Output:
# Amit 85 Pune
# Priya 90 Mumbai
# Rahul 78 Delhi

#------------------------------------------------------------------------------------------------------

a = [1, 2, 3]
b = ['x', 'y']
 
print("\nZipping lists of different lengths:")
print(list(zip(a, b)))
 
# Expected Output:
# [(1, 'x'), (2, 'y')]
#------------------------------------------------------------------------------------------------------

names = ['Amit', 'Priya', 'Rahul']
marks = [85, 90, 78]

print("\nCreating a dictionary using zip:")
student_dict = dict(zip(names, marks))
print(student_dict)
 
# Expected Output:
# {'Amit': 85, 'Priya': 90, 'Rahul': 78}

