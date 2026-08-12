"""
============================================================
INHERITANCE
============================================================
What is Inheritance?
Inheritance is a feature of Python that allows a child class
to access the properties and methods of a parent class.

Why do we use Inheritance?
1. Code Reusability
2. Reduce Code Duplication
3. Easy Maintenance
4. Extensibility

Advantages of Inheritance:
1. We can reuse existing code.
2. It reduces code duplication.
3. It makes code easier to maintain.
4. We can add new features to the child class.

Important Terms:
Parent Class:
The class whose properties and methods are inherited
by another class.

Child Class:
The class that inherits properties and methods
from the parent class.

Inherited Method:
A method that a child class gets from its parent class.

Syntax:
class Child(Parent):
    pass

Interview Answer:
What is Inheritance?
"Inheritance is a feature of Python that allows a child class
to access the properties and methods of a parent class."

Why do we use Inheritance?
"We use inheritance mainly for code reusability and
to reduce code duplication."

Advantages:
"The main advantages of inheritance are code reusability,
reduced code duplication, easy maintenance, and extensibility."

============================================================
"""
# Parent Class
class P:

    # Instance Method of Parent Class
    def m1(self):
        print("m1 method")

    # Instance Method of Parent Class
    def m2(self):
        print("m2 method")


# Creating the first object of Parent Class
p1 = P()

# Calling m1() method using p1 object
p1.m1()


# Creating the second object of Parent Class
p2 = P()

# Calling m1() method using p2 object
p2.m1()


# Child Class
# C inherits from Parent Class P
class C(P):

    # Instance Method of Child Class
    def m3(self):
        print("m3 method")

    # Instance Method of Child Class
    def m4(self):
        print("m4 method")


# Creating an object of Child Class
c1 = C()

# Calling m3() method of Child Class
c1.m3()

# Calling m4() method of Child Class
c1.m4()

#-------------------------------------------------------------------------------







