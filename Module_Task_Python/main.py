import bank_utils
# ---------------------------------------
# Part 1 - Testing Functions
# ---------------------------------------

print("----- FUNCTION TESTING -----")

# 1. Mask Account
print("Masked Account:",
      bank_utils.mask_account("123456789012"))


# 2. Count Digits
print("Number of Digits:",
      bank_utils.count_digits("123456789"))


# 3. Count Uppercase and Lowercase
upper, lower = bank_utils.count_upper_lower("Ram Pune")

print("Uppercase:", upper)
print("Lowercase:", lower)


# 4. Validate PIN
print(bank_utils.validate_pin("1234"))
print(bank_utils.validate_pin("12a4"))


# 5. Calculate Interest
print("Simple Interest:",
      bank_utils.calculate_interest(50000, 6, 2))


# 6. Transaction Limit
print(bank_utils.check_transaction_limit(5000))
print(bank_utils.check_transaction_limit(25000))
print(bank_utils.check_transaction_limit(75000))
print(bank_utils.check_transaction_limit(150000))


# 7. Count Transactions
transactions = [5000, 2000, 8000, 15000]

print("Total Transactions:",
      bank_utils.count_transactions(transactions))


# 8. Calculate Balance
transactions = [10000, -2000, 5000, -1000]

print("Calculated Balance:",
      bank_utils.calculate_balance(transactions))

# ---------------------------------------
# Part 2 - Create Bank Accounts
# ---------------------------------------

print("\n----- BANK ACCOUNT TESTING -----")

account1 = bank_utils.BankAccount(
    "Pavan",
    "123456789012",
    50000
)

account2 = bank_utils.BankAccount(
    "Rahul",
    "987654321098",
    25000
)

account3 = bank_utils.BankAccount(
    "Amit",
    "12345",
    5000
)

# ---------------------------------------
# Part 3 - Deposit
# ---------------------------------------

print("\n----- DEPOSIT -----")

account1.deposit(5000)
account2.deposit(10000)

print("Account 1 Balance:", account1.check_balance())
print("Account 2 Balance:", account2.check_balance())

# ---------------------------------------
# Part 4 - Withdrawal
# ---------------------------------------

print("\n----- WITHDRAWAL -----")

print(account1.withdraw(3000))
print("Account 1 Balance:", account1.check_balance())

print(account2.withdraw(5000))
print("Account 2 Balance:", account2.check_balance())

# ---------------------------------------
# Part 5 - Insufficient Balance
# ---------------------------------------

print("\n----- INSUFFICIENT BALANCE TEST -----")

print(account3.withdraw(10000))

# ---------------------------------------
# Part 6 - Account Validation
# ---------------------------------------

print("\n----- ACCOUNT VALIDATION -----")

print("Account 1:", account1.is_valid_account())
print("Account 2:", account2.is_valid_account())
print("Account 3:", account3.is_valid_account())

# ---------------------------------------
# Part 7 - Account Summaries
# ---------------------------------------

print("\n----- ACCOUNT SUMMARIES -----")

print("\nAccount 1")
print(account1.account_summary())

print("\nAccount 2")
print(account2.account_summary())

print("\nAccount 3")
print(account3.account_summary())