class Bank:
    def __init__(self,ac,nm,bal):
        self.account = ac
        self.name = nm
        self.bal = bal

class Saving_account(Bank):
    rate = 5
    def __init__(self,ac,nm,bal,adh,mob):
        super().__init__(ac,nm,bal)
        self.adhar = adh
        self.mobile = mob

s1 = Saving_account(191,"vaibhav patil",30000, 123456789012, 9876543210)

