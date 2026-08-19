"""
Enumerate:------------>>
- enumerate() lets you loop over a sequence (list, tuple, string, etc.)
  while automatically keeping track of the index of each item.
- No need to manually create/increment a counter variable.
 
SYNTAX:
    enumerate(iterable, start=0)
 
    iterable -> the sequence you want to loop over
    start    -> number to begin counting from (default = 0)
"""

students = ["om","ganesh","ram","arun"]
e_obj = enumerate(students)
print(e_obj)
l = list(e_obj)
print(l)
for index,name in l:
    print(index,name)


students = ["om","ganesh","ram","arun"]
# for index,name in enumerate(students,101):  # start index - 101
for index,name in enumerate(students):  # start index - 0
    print(index,name)

fruits = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(fruits, start=1):  # start=1
    print(index, fruit)

