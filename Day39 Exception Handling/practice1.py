n1 = int(input("Num1: "))   # 10
n2 = int(input("Num2: "))   # 0
sum = n1 + n2
print(sum)                  # 10

try:
    div = n1 / n2            # ZeroDivisionError (ZDE)
    print(div)
except:
    print("we cant divide any number by ZERO")

mul = n1 * n2
print(mul)
print("End")
print()

#------------------------------------------------------------------------------------------------------

n1 = int(input("Num1: "))   # 10
n2 = int(input("Num2: "))   # 0
sum = n1 + n2                # 10
mul = n1 * n2                # 0

try:
    div = n1 / n2             # ZeroDivisionError
except:
    print("cant divide by zero")
else:
    print("division: ", div)
finally:
    print("mul: ", mul)
    print("sum:", sum)
print()

#------------------------------------------------------------------------------------------------------

n1 = 10
n2 = '8'    # note: this is a STRING, not an integer

try:
    div = n1 / n2       # 10 / '8' → error!
    print(div)
except ZeroDivisionError:
    print("cant divide by zero")
except TypeError:
    print("type error")

print("code....")
print()
#------------------------------------------------------------------------------------------------------

n1 = 10
n2 = '9'   # string again

try:
    div = n1 / n2       # int / str → error!
    print(div)
except Exception as e:
    print(e)

print("coding...")
print()

#-----------------------------------------------------------------------------------

# raise:
age = int(input("Enter Age: "))
if age < 0:
    raise ValueError("Negative age")
print("My age is", age)
print()
#-----------------------------------------------------------------------------------

class InvalidPasswordError(Exception):
    pass
password = input("Enter New Password: ")
if len(password) < 8:
    raise InvalidPasswordError("Length Must be 8 char")
print("Done")
print()
#-----------------------------------------------------------------------------------




