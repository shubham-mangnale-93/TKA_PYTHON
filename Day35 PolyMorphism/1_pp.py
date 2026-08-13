# Operator Overloading / Magic Methods (Dunder Methods):----->>>
class Book:
    def __init__(self,bn,pr,pg):
        self.bname = bn
        self.price  =pr
        self.pages =pg
    def __add__(self,other):
        return self.price + other.price

b1 = Book("Python",1000,100)
b2= Book("Java",1500,150)
 
print(b1+b2)  #add
print(b1.__add__(b2))

#----------------------------------------------------------------------------------------

class Hotel:
    def __init__(self, hn, rate):
        self.hotel_name = hn
        self.rate = rate

    def __gt__(self, other):
        if self.rate > other.rate:
            print(f'Yes, {self.hotel_name} is more expensive than {other.hotel_name}')
        else:
            print(f'No, {other.hotel_name} is more expensive than {self.hotel_name}')


h1 = Hotel("Tiranga Hotel", 2000)
h2 = Hotel("Taj Hotel", 5000)

print(h1 > h2)
print(h2 > h1)
#----------------------------------------------------------------------------------------

# Method Overloading:--------->>

#----------------------------------------------------------------------------------------

# Method Overriding:--------->>

#----------------------------------------------------------------------------------------

# Variable Overriding:----------->>

#----------------------------------------------------------------------------------------

class A:
    num = 100
    def m1(self):
        print("Hii,i am m1 method")
    def m2(self):
        print("Hii,i am m2 method")
    def m3(self):
        print("Hii,i am m3 method of A class")


class B(A):
    num = 150
    def m3(self):
        print("hii,i am m3 method of B class")


b1 = B()
a1 = A()

b1.m3()

print(a1.num)   # 100
print(b1.num)   # 150  





































