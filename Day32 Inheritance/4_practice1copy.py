"""
============================================================
ACCOUNT MANAGEMENT SYSTEM
============================================================

This program demonstrates:

1. Class
2. Class Attributes
3. Instance Attributes
4. Constructor
5. Instance Methods
6. Inheritance
7. Code Reusability
8. Type Checking using isinstance()
9. Default Argument
10. Child Class
11. Child Class Methods
============================================================
"""


# ============================================================
# PARENT CLASS
# ============================================================

class Account:

    # Class Attributes
    # These values are common for all Account objects
    bank_name = "Bank Of Maharashtra"
    branch_name = "Karve Nagar, Pune"
    ifsc_code = "MAH00256"


    # Constructor
    # It is automatically called when an object is created
    def __init__(self, ac, nm, bal=0):

        # Instance Attributes
        # These values are different for each object
        self.account_no = ac
        self.name = nm
        self.balance = bal


    # Instance Method
    # Displays account details
    def show_details(self):

        print(f'''
        Bank Name : {Account.bank_name}
        Branch : {Account.branch_name}
        IFSC CODE : {Account.ifsc_code}
        Name : {self.name}
        Account No : {self.account_no}
        Balance : {self.balance}
        ''')


    # Instance Method
    # Displays the current balance
    def check_balance(self):

        print(f"Available Balance : {self.balance}")


    # Instance Method
    # Deposits money into the account
    def deposit(self, amount):

        # Check whether amount is int or float
        if isinstance(amount, (int, float)):

            # Check whether amount is positive
            if amount > 0:

                self.balance = self.balance + amount
                return "done"

            else:
                return "enter positive value only"

        else:
            return "enter numeric value only"


    # Instance Method
    # Withdraws money from the account
    def withdraw(self, amount):

        # Check whether amount is int or float
        if isinstance(amount, (int, float)):

            # Check whether amount is positive
            if amount > 0:

                # Check whether sufficient balance is available
                if amount <= self.balance:

                    self.balance -= amount
                    return "done"

                return "insufficient balance"

            else:
                return "enter positive number"

        else:
            return "enter numeric value only"


# ============================================================
# CREATING OBJECTS OF PARENT CLASS
# ============================================================

# Creating first Account object
ac1 = Account(12345678910, "Shubham Patil", 50000)

# Creating second Account object
ac2 = Account(25678926262, "Priyanka Patil", 500)


# Checking balance of ac1
ac1.check_balance()

# Depositing money into ac1
print(ac1.deposit(20000))

# Checking balance after deposit
ac1.check_balance()

# Trying to withdraw a negative amount
ac1.withdraw(-5000)

# Withdrawing 5000 from ac1
print(ac1.withdraw(5000))

# Checking balance after withdrawal
ac1.check_balance()


print("--" * 30)


# Trying to withdraw 2500 from ac2
# ac2 has only 500 balance
print(ac2.withdraw(2500))

# Checking ac2 balance
ac2.check_balance()


print()


# ============================================================
# CHILD CLASS
# ============================================================

# Saving_Account is a Child Class
# Account is the Parent Class
#
# Saving_Account inherits the methods and attributes
# of the Account class.
class Saving_Account(Account):

    # Class Attribute of Child Class
    interest_rate = 5


    # Instance Method of Child Class
    # Calculates interest based on current balance
    def cal_interest(self):

        interest_amount = self.balance * Saving_Account.interest_rate / 100

        return interest_amount


    # Instance Method of Child Class
    # Adds calculated interest to the balance
    def add_interest(self):

        interest_amount = self.cal_interest()

        self.balance += interest_amount

        return "done"


# ============================================================
# CREATING OBJECT OF CHILD CLASS
# ============================================================

# Creating object of Saving_Account class
s1 = Saving_Account("76567377337", "Kunal Kale", 45000)


# check_balance() is inherited from Account class
s1.check_balance()

# deposit() is inherited from Account class
s1.deposit(5000)

# Checking balance after deposit
s1.check_balance()

# withdraw() is inherited from Account class
s1.withdraw(7000)

# Checking balance after withdrawal
s1.check_balance()

# show_details() is inherited from Account class
s1.show_details()


# Checking balance before adding interest
s1.check_balance()

# Calling Child Class method
s1.add_interest()

# Checking account details after adding interest
s1.show_details()

