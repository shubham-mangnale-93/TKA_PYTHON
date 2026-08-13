# Multilevel Inheritance + MRO (Method Resolution Order):----->>
class C1:
    def m1(self):
        print("m1 method")
# c1 = C1() 
# c1.m1()

class C2 (C1):
    def m2(self):
        print("m2 method")   
# c2 = C2()
# c2.m2()
# c2.m1()
        
class C3(C2):
    def m3(self):
        print("m3 method")
# c3 = C3()
# c3.m3()
# c3.m2()
# c3.m1()

class C4(C3):
    def m4(self):
        print("m4 method")
c4 = C4()
c4.m4()
c4.m3()
# c4.m2()
# c4.m1()

print(C4.__mro__)  #(<class '__main__.C4'>, <class '__main__.C3'>, <class '__main__.C2'>, <class '__main__.C1'>, <class 'object'>)

"""
============================================================
                INHERITANCE IN PYTHON
============================================================
What is Inheritance?
Inheritance is a feature of Python that allows a child class
to access the properties and methods of a parent class.

Simple Definition:
A child class can reuse the properties and methods
of a parent class.

Why do we use Inheritance?
1. Code Reusability
2. Reduce Code Duplication
3. Easy Maintenance
4. Extensibility

Advantages of Inheritance:
1. Code Reusability
2. Less Code Duplication
3. Easy Maintenance
4. Code Extensibility

============================================================
TYPES OF INHERITANCE
============================================================
1. Single Inheritance
2. Multilevel Inheritance
3. Multiple Inheritance
4. Hierarchical Inheritance

Note:
Hybrid Inheritance is also possible in Python by combining
different types of inheritance.

============================================================
1. SINGLE INHERITANCE
============================================================
Definition:
Single inheritance is a type of inheritance where
one child class inherits from one parent class.

Structure:
    Parent
       |
       ↓
     Child

Interview Answer:
"Single inheritance is a type of inheritance where
one child class inherits from one parent class."

============================================================
PROGRAM
============================================================
"""
# Parent Class
class Parent:

    def m1(self):
        print("Parent method")


# Child Class
# Child inherits from Parent
class Child(Parent):

    def m2(self):
        print("Child method")

# Creating object of Child Class
c1 = Child()

# Calling inherited method from Parent
c1.m1()

# Calling Child Class method
c1.m2()

"""
============================================================
2. MULTILEVEL INHERITANCE
============================================================
Definition:
Multilevel inheritance is a type of inheritance where
a class inherits from another class, which itself
inherits from another class.

Structure:
    C1
    ↓
    C2
    ↓
    C3
    ↓
    C4

Interview Answer:
"Multilevel inheritance is a type of inheritance where
a class inherits from another class, which itself
inherits from another class."
============================================================
PROGRAM
============================================================
"""
# Parent Class
class C1:

    def m1(self):
        print("m1 method")


# C2 inherits from C1
class C2(C1):

    def m2(self):
        print("m2 method")


# C3 inherits from C2
class C3(C2):

    def m3(self):
        print("m3 method")


# C4 inherits from C3
class C4(C3):

    def m4(self):
        print("m4 method")


# Creating object of C4
c4 = C4()

# Calling C4 method
c4.m4()

# Calling inherited method from C3
c4.m3()

# Calling inherited method from C2
c4.m2()

# Calling inherited method from C1
c4.m1()


"""
============================================================
3. MRO - METHOD RESOLUTION ORDER
============================================================
MRO stands for Method Resolution Order.
Definition:

MRO is the order in which Python searches for a method
or attribute in the inheritance hierarchy.

For the above example:
C4 → C3 → C2 → C1 → object

Python searches for a method in this order.

We can check MRO using:
ClassName.mro()

or

ClassName.__mro__

Important:
MRO is NOT a type of inheritance.
It is a method/attribute search order used by Python.

Interview Answer:

"MRO stands for Method Resolution Order. It defines
the order in which Python searches for methods and
attributes in a class hierarchy."

============================================================
PROGRAM
============================================================
"""


# Checking MRO
print(C4.mro())

# Another way to check MRO
print(C4.__mro__)


"""
============================================================
4. MULTIPLE INHERITANCE
============================================================
Definition:

Multiple inheritance is a type of inheritance where
a single child class inherits from multiple parent classes.

Simple Definition:

Multiple Parents → One Child

Structure:

       Parent1       Parent2
          \             /
           \           /
              Child

Interview Answer:

"Multiple inheritance is a type of inheritance where
a single child class inherits from multiple parent classes."

============================================================
PROGRAM
============================================================
"""
# Parent Class 1
class Parent1:

    def m1(self):
        print("Parent1 method")


# Parent Class 2
class Parent2:

    def m2(self):
        print("Parent2 method")


# Child Class
# Child inherits from both Parent1 and Parent2
class Child(Parent1, Parent2):

    def m3(self):
        print("Child method")


# Creating object of Child Class
c1 = Child()

# Calling method from Parent1
c1.m1()

# Calling method from Parent2
c1.m2()

# Calling method from Child
c1.m3()


# Checking MRO
print(Child.mro())


"""
============================================================
5. HIERARCHICAL INHERITANCE
============================================================
Definition:
Hierarchical inheritance is a type of inheritance where
multiple child classes inherit from a single parent class.

Simple Definition:
One Parent → Multiple Children

Structure:

             Parent
             /    \
            /      \
        Child1    Child2

Interview Answer:

"Hierarchical inheritance is a type of inheritance where
multiple child classes inherit from a single parent class."

============================================================
PROGRAM
============================================================
"""
# Parent Class
class Parent:

    def m1(self):
        print("Parent method")


# Child Class 1
# Child1 inherits from Parent
class Child1(Parent):

    def m2(self):
        print("Child1 method")


# Child Class 2
# Child2 inherits from Parent
class Child2(Parent):

    def m3(self):
        print("Child2 method")


# Creating object of Child1
c1 = Child1()

# Calling inherited method from Parent
c1.m1()

# Calling Child1 method
c1.m2()


# Creating object of Child2
c2 = Child2()

# Calling inherited method from Parent
c2.m1()

# Calling Child2 method
c2.m3()


"""
============================================================
6. HYBRID INHERITANCE
============================================================
Definition:
Hybrid inheritance is a combination of two or more
types of inheritance.

It can combine types such as:
1. Multiple Inheritance
2. Multilevel Inheritance
3. Hierarchical Inheritance

Simple Definition:
Combination of different types of inheritance
is called Hybrid Inheritance.

Example Structure:

             A
            / \
           B   C
            \ /
             D

============================================================
PROGRAM
============================================================
"""
# Parent Class
class A:

    def m1(self):
        print("A method")


# Child Class
class B(A):

    def m2(self):
        print("B method")


# Child Class
class C(A):

    def m3(self):
        print("C method")


# D inherits from both B and C
class D(B, C):

    def m4(self):
        print("D method")


# Creating object of D
d1 = D()

# Calling method from A
d1.m1()

# Calling method from B
d1.m2()

# Calling method from C
d1.m3()

# Calling method from D
d1.m4()


# Checking MRO
print(D.mro())


"""
============================================================
QUICK REVISION
============================================================
1. Single Inheritance
One Parent → One Child

2. Multilevel Inheritance
Parent → Child → Child

3. Multiple Inheritance
Multiple Parents → One Child

4. Hierarchical Inheritance
One Parent → Multiple Children

5. Hybrid Inheritance
Combination of two or more types of inheritance

6. MRO
Method Resolution Order
MRO defines the order in which Python searches
for methods and attributes.

============================================================
INTERVIEW QUICK ANSWERS
============================================================

What is Inheritance?
"Inheritance is a feature of Python that allows a child
class to access the properties and methods of a parent class."

Why do we use Inheritance?
"We use inheritance mainly for code reusability and
to reduce code duplication."

What is Single Inheritance?
"One child class inherits from one parent class."

What is Multilevel Inheritance?
"A class inherits from another class, which itself
inherits from another class."

What is Multiple Inheritance?
"One child class inherits from multiple parent classes."

What is Hierarchical Inheritance?
"Multiple child classes inherit from a single parent class."

What is Hybrid Inheritance?
"Hybrid inheritance is a combination of two or more
types of inheritance."

What is MRO?
"MRO stands for Method Resolution Order. It defines
the order in which Python searches for methods and
attributes in a class hierarchy."

============================================================
"""