from account import Account

class Saving_Account(Account):

    def add_interest(self):

        interest = self.balance * 5/100
        self.balance += interest

        print("Interest Added:", interest)
        print("New Balance:", self.balance)

    def apply_for_loan(self):

        if self.balance >= 10000:
            print("Loan Application Submitted")
        else:
            print("Minimum balance of 10000 is required for loan")

            