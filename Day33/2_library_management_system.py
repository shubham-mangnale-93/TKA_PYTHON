class Library:
    def __init__(self,ln):
        self.library_name = ln
        self.books = {}   # {"python":10,"java":5}
        self.members = {}  # {"yogesh":["python","java"], "om":["python"]}

    def add_book(self,bn,count):
        # var[k] = value
        if bn in self.books:
            self.books[bn] = self.books[bn] + count   
        else:
            self.books[bn] = count
        return "done"

    def remove_book(self,bn,count):
        if bn in self.books:
            self.books[bn] = self.books[bn]-count
            if self.books[bn]==0:
                self.books.pop(bn)
            return "done"    
        else:
            print("")


    def display_books(self):
        for bn,c in self.books.items():
            print(f'{bn} - {c}')

    def issue_book(self,mname,bname):
        if bname in self.books:
            self.books[bname] = self.books[bname]-1
            if mname not in self.books:
                self.members[mname] = [bname] 
            else:
                self.members[mname].append(bname)
            return "done"
        else:
            return "not available"

    def return_book(self,mname,bname):
        if mname in self.members and bname in self.members[mname]:
            self.members[mname].remove(bname)
            self.books[bname] = self.books[bname] +1
            return "done"    

# l1 = Library("TKA")
# l2 = Library("JBK")

member = {"yogesh":["java"],"om":["python"]}
print("om" in member)
print("raj" in member)

print("java" in member["yogesh"])

print(member["yogesh"])




