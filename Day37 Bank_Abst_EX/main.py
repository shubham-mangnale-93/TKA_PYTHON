from saving_account import Saving_Account
from current_account import Current_Account

s1 = Saving_Account(101, "Maroti Patil", 30000)
print(" Saving Account ".center(30, "-"))

s1.check_balance()
s1.deposit(5000)
s1.withdraw(10000)
s1.add_interest()
s1.apply_for_loan()
print()
#----------------------------------------------------------

c1 = Current_Account(102, "Rahul Patil", 60000)
print(" Current Account ".center(30, "-"))

c1.check_balance()
c1.deposit(10000)
c1.withdraw(20000)
c1.add_interest()
c1.apply_for_loan()


