class Account:
    bank_name = "Bank Of Maharashtra"
    branch_name = "Karve Nagar, Pune"
    ifsc_code = "MAH00256"

    def __init__(self,ac,nm,bal=0):
        # instance
        self.account_no = ac
        self.name = nm
        self.balance = bal

    def show_details(self):
        print(f'''
        Bank Name : {Account.bank_name}
        Branch : {Account.branch_name}
        IFSC CODE : {Account.ifsc_code}
        Name : {self.name}
        Account No : {self.account_no}
        Balance : {self.balance}
        
        ''')

    def check_balance(self):
        print(f"Available Balance : {self.balance}")

    def deposit(self,amount):
        if isinstance(amount,(int,float)):     
                      if amount>0:
                             self.balance = self.balance + amount
                             return "done"
                      else:
                            return "enter positive value only"
        else:
              return "enter numeric value only"

    def withdraw(self,amount):
          if isinstance(amount,(int,float)):
                    if amount>0:
                            if amount<=self.balance:
                                self.balance -= amount
                                return "done"
                            return "insufficient balance"
                    else:
                            return "enter positive number"

          else:
               return "enter numeric value only" 
                
            
ac1 = Account(12345678910,"Shubham Patil",50000) 
ac2 = Account(25678926262,"Priyanka Patil",500)      
ac1.check_balance()
print(ac1.deposit(20000))
ac1.check_balance()   
ac1.withdraw(-5000)
print(ac1.withdraw(5000))
ac1.check_balance()

print("--"*30)
print(ac2.withdraw(2500))
ac2.check_balance()
#---------------------------------------------------------------------------
print()
class Saving_Account(Account):
      interest_rate = 5

      def cal_interest(self):
            interest_amount = self.balance *Saving_Account.interest_rate/100
            return interest_amount

      def add_interest(self):
            interest_amount = self.cal_interest()
            self.balance += interest_amount
            return  "done"
            


s1 = Saving_Account("76567377337","Kunal Kale", 45000)
s1.check_balance()
s1.deposit(5000)
s1.check_balance()
s1.withdraw(7000)
s1.check_balance()
s1.show_details()


s1.check_balance()
s1.add_interest()
s1.show_details()





