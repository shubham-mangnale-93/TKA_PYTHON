'''
# Abstraction:------->>>
: Abstraction is the process of hiding implementation details and 
  showing only essential features to the user. 
  In Python, abstraction can be implemented using abstract classes and abstract methods.

# Real-life example:------->>>
: For example, an ATM shows options like withdraw and deposit, 
  but it hides the internal transaction process from the user.

#Syntax:------>>>
from abc import ABC, abstractmethod

class ClassName(ABC):

    @abstractmethod
    def method_name(self):
        pass
#------------------------------------------------------------
# ABC              → Abstract Base Class
# @abstractmethod  → Abstract method      
#------------------------------------------------------------
'''
# Example:-------->>
from abc import ABC,abstractmethod
class X(ABC):

    @abstractmethod
    def m1(self):
        pass

    @abstractmethod
    def m1(self):
        pass

    @abstractmethod
    def m1(self):
        pass
    

 















