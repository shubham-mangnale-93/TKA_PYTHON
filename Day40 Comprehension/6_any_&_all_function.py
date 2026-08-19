"""
====================================================
NOTES: any() and all() functions in Python
====================================================
 
- any() -> Returns True if AT LEAST ONE element in the
           iterable is True. Returns False if ALL are False.
 
- all() -> Returns True only if ALL elements in the
           iterable are True. Returns False if EVEN ONE is False.
 
Both are commonly used with list comprehensions that produce
a list of True/False values.
"""

numbers = [1, 11, 22, 33, 44, 55, 46, 65]
# any:------->>>
print(any([True if num > 60 else False for num in numbers]))
print(any([num > 60 for num in numbers]))

# all:------->>>
print(all([num > 10 for num in numbers]))


