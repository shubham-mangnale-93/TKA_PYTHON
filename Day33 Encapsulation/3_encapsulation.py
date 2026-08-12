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

