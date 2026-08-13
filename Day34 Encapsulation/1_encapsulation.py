"""
============================================================
ENCAPSULATION
============================================================
# What is Encapsulation?
Encapsulation is the process of wrapping data and methods
into a single unit, such as a class, and restricting direct
access to the data.
  
# Why do we use Encapsulation?
1. Data Hiding
2. Data Protection
3. Controlled Access
4. Better Security
5. Easy Maintenance

# Important Point:
Encapsulation = Data + Methods + Data Protection

# In Python:
We can use private attributes to restrict direct access
to data.

# Private attribute syntax:
__variable_name


Example:
class Account:

    def __init__(self, balance):
        self.__balance = balance

    def check_balance(self):
        print(self.__balance)


Here:
__balance
    ↓
Private Instance Attribute

check_balance()
    ↓
Method used to access the data

Account
    ↓
Class that contains both data and methods

#-Why is Encapsulation used?
"Encapsulation is used for data hiding, data protection,
controlled access, and better security."
 
============================================================
"""
# public attribute:----->>
class Machine:
    brand_name = "Tejas"        # class attribute — shared by ALL objects

    def __init__(self, mn):
        # instance attributes — unique to each object
        self.mname = mn
        self.in_count = 0
        self.out_count = 0

    def display_count(self):
        print(f'''
        Welcome to {self.mname}
        In Count : {self.in_count}
        Out Count : {self.out_count}
        ''')

    def inc_in(self):
        self.in_count += 1

    def inc_out(self):
        self.out_count += 1

    def reset(self):
        self.in_count = 0
        self.out_count = 0

dmart = Machine("dmart")
zudio = Machine("zudio")


dmart.display_count()

dmart.inc_in()
dmart.inc_in()
dmart.inc_in()
dmart.inc_in()
dmart.display_count()

dmart.inc_out()
dmart.inc_out()
dmart.display_count()

print(dmart.in_count)     # we can access public attributes outside of class
dmart.in_count = 999      # we can also change them directly
dmart.display_count()

#--------------------------------------------------------------------------------------------
# Private attribute :------->>>
class Machine:

    def __init__(self, mn):
        self.mname = mn
        self.__in_count = 0
        self.__out_count = 0

    def display_count(self):
        print(f"""
        Welcome to {self.mname}
        In Count : {self.__in_count}
        Out Count : {self.__out_count}
        """)

    def inc_in(self):
        self.__in_count += 1

    def inc_out(self):
        self.__out_count += 1

    def reset(self):
        self.__in_count = 0
        self.__out_count = 0


dmart = Machine("dmart")

dmart.display_count()

dmart.inc_in()
dmart.inc_in()
dmart.inc_in()

dmart.inc_out()
dmart.inc_out()

dmart.display_count()
 
print(dmart.__in_count)   # AttributeError
dmart.__in_count = 999    
dmart.display_count()
