
# Dic comp:-------->>
'''
new_dict = {k:v for var in iterable}
new_dict = {k:v for var in iterable if con}
new_dict = {k:v if con else v for var in iterable}
'''
numbers = [1,2,3,4,5,6]
square = {num:num**2 for num in numbers}
print(square)

numbers = [1,2,3,4,5,6]
odd_square = {num:num**2 for num in numbers if num%2==1}
print(odd_square)

numbers = [1,2,3,4,5,6]
result = {num:num**2 if num%2==0 else num**3 for num in numbers}
print(result)
#------------------------------------------------------------------------------------------------------

product_mrp = {"p1":6000,"p2":2000,"p3":7000,"p4":8000,"p5":1000,"p6":2500}
# create new dic--->sp---->dis mrp > 5000---->15% mrp<=5000 ---->10%
product_sp = {pname:mrp-mrp*15/100 if mrp>5000 else mrp-mrp*10/100  for pname,mrp in product_mrp.items()}
print(product_sp)