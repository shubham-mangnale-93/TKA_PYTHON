'''
Bank_Project
│
├── account.py
├── saving_account.py
└── current_account.py
'''
#----------------------------------------
from abc import ABC,abstractmethod
class Account(ABC):

    def __init__(self, account_number,name,balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def check_balance(self):
        print("Account Number:", self.account_number)
        print("Name:", self.name)
        print("Balance:", self.balance)

    def deposit(self,amount):

        if amount > 0:
            self.balance += amount
            print("Amount Deposited:", amount)
            print("New Balance:", self.balance)
        else:
            print("Invalid Deposit Amount")

    def withdraw(self,amount):

        if amount > 0:

            if amount <= self.balance:
                self.balance -= amount
                print("Amount Withdrawn:", amount)
                print("Remaining Balance:", self.balance)
            else:
                print("Insufficient Balance")
        else:
            print("Invalid Withdrawal Amount")

    @abstractmethod
    def add_interest(self):
        pass

    @abstractmethod
    def apply_for_loan(self):
        pass

