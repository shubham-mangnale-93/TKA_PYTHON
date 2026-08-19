# List Comp:----->>

# 1. syntax : new_list [exp for var in iterable]
numbers = [10,20,30,40,50]
half = [num/2 for num in numbers]
print(half)

# 2. syntax : new_list [exp for var in iterable if con]
numbers = [1,2,3,4,5]
square = [num**2 for num in numbers if num%2==0]
print(square)

# 3. syntax : new_list [exp1 if cond else e2 for var in iterable ]
numbers = [1,2,3,4,5]
result = [num**2 if num%2==0 else num**3 for num in numbers]
print(result)

#------------------------------------------------------------------------------------------------------

 
 
 












