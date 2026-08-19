
# Set Comp:------->>

# 1. syntax : new_set {exp for var in iterable}
numbers = [10,25,35,40,50]
result = {num/2 for num in numbers}


# 2. syntax : new_set{exp for var in iterable if con}
numbers = [1,2,3,4,5]
square = {num*2 for num in numbers if num%2==0}
print(square)


# 3. syntax : new_list {exp1 if cond else e2 for var in iterable}
numbers = [1,2,3,4,5]
result = {num**2 if num%2==0 else num**3 for num in numbers}
print(result)

# ex:---->>>
names = ["Amit","sham","Anurag","Sumit"]
result = {name for name in names if name.startswith("A")}
print(result)

#------------------------------------------------------------------------------------------------------


salary = {"mayur": 60000, "mayuri": 40000, "tushar": 6000,
          "aniket": 40000, "rehan": 70000}

# ----------------------------------------------------
# 1) BASIC SET COMPREHENSION
#    Syntax: {exp for var in iterable}
# ----------------------------------------------------
emp_name = {name for name in salary}
print("Basic set comprehension (all names):")
print(emp_name)
 
# Expected Output:
# {'mayur', 'mayuri', 'tushar', 'aniket', 'rehan'}
# (Order may vary since sets are unordered)
 
 
# ----------------------------------------------------
# 2) SET COMPREHENSION WITH CONDITION (filter)
#    Syntax: {exp for var in iterable if cond}
# ----------------------------------------------------
sal_less = {name for name in salary if salary[name] < 50000}
print("\nNames with salary less than 50000:")
print(sal_less)
 
# Expected Output:
# {'mayuri', 'tushar', 'aniket'}
# Reason:
#   mayuri -> 40000  (< 50000) YES
#   tushar -> 6000   (< 50000) YES
#   aniket -> 40000  (< 50000) YES
#   mayur  -> 60000  (< 50000) NO
#   rehan  -> 70000  (< 50000) NO
 
 
# ----------------------------------------------------
# 3) SET COMPREHENSION WITH IF-ELSE (ternary expression)
#    Syntax: {e1 if cond else e2 for var in iterable}
# ----------------------------------------------------
x = {name.upper() if salary[name] > 50000 else name.lower() for name in salary}
print("\nUPPERCASE if salary > 50000, else lowercase:")
print(x)
 
# Expected Output:
# {'MAYUR', 'mayuri', 'tushar', 'aniket', 'REHAN'}
# Reason:
#   mayur  -> 60000 (> 50000) -> "MAYUR" (uppercase)
#   rehan  -> 70000 (> 50000) -> "REHAN" (uppercase)
#   mayuri -> 40000 (not > 50000) -> "mayuri" (lowercase)
#   tushar -> 6000  (not > 50000) -> "tushar" (lowercase)
#   aniket -> 40000 (not > 50000) -> "aniket" (lowercase)


