# 
            #: Task: Banking Utility Module
# 
# 1. Mask Account Number
def mask_account(account_no):
    return "*" * (len(account_no) - 4) + account_no[-4:]

# 2. Count Digits
def count_digits(account_no):
    count = 0

    for ch in account_no:
        if ch.isdigit():
            count += 1

    return count

# 3. Count Uppercase and Lowercase
def count_upper_lower(text):
    upper = 0
    lower = 0

    for ch in text:
        if ch.isupper():
            upper += 1
        elif ch.islower():
            lower += 1

    return upper, lower

# 4. Validate PIN
def validate_pin(pin):
    if len(pin) == 4 and pin.isdigit():
        return "Valid PIN"
    else:
        return "Invalid PIN"

# 5. Calculate Simple Interest
def calculate_interest(balance, rate, years):
    interest = (balance * rate * years) / 100
    return interest

# 6. Check Transaction Limit
def check_transaction_limit(amount):

    if amount <= 10000:
        return "Small Transaction"

    elif amount <= 50000:
        return "Medium Transaction"

    elif amount <= 100000:
        return "Large Transaction"

    else:
        return "High Value Transaction"

# 7. Count Transactions
def count_transactions(transactions):
    return len(transactions)

# 8. Calculate Balance
def calculate_balance(transactions):

    balance = 0

    for amount in transactions:
        balance = balance + amount

    return balance


# ------------------------------------------------
# BankAccount Class
# ------------------------------------------------
class BankAccount:

    # Constructor
    def __init__(self, account_holder, account_no, balance):

        self.account_holder = account_holder
        self.account_no = account_no
        self.balance = balance


    # 1. Deposit
    def deposit(self, amount):

        self.balance = self.balance + amount


    # 2. Withdraw
    def withdraw(self, amount):

        if amount > self.balance:
            return "Insufficient Balance"

        else:
            self.balance = self.balance - amount
            return "Withdrawal Successful"


    # 3. Check Balance
    def check_balance(self):

        return self.balance


    # 4. Validate Account
    def is_valid_account(self):

        if len(self.account_no) == 12 and self.account_no.isdigit():
            return "Valid Account"

        else:
            return "Invalid Account"


    # 5. Account Category
    def account_category(self):

        if self.balance < 10000:
            return "Basic"

        elif self.balance < 50000:
            return "Standard"

        elif self.balance < 100000:
            return "Premium"

        else:
            return "Elite"


    # 6. Account Summary
    def account_summary(self):

        # return (
        #     "Account Holder: " + self.account_holder +
        #     "\nAccount Number: " + mask_account(self.account_no) +
        #     "\nBalance: " + str(self.balance) +
        #     "\nCategory: " + self.account_category() +
        #     "\nAccount Status: " + self.is_valid_account()
        # )

 

      return f'''Account Holder: {self.account_holder}
Account Number: {mask_account(self.account_no)}
Balance: {self.balance}
Category: {self.account_category()}
Account Status: {self.is_valid_account()}
'''