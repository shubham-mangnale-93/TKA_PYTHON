'''
Encapsulation (Getter-Setter):----->>


'''
class Student:
    def __init__(self, nm, ag, mk):
        self.__name = nm
        self.__age = ag
        self.__marks = mk

    def details(self):
        print(f'''
        Name  : {self.__name}
        Age   : {self.__age}
        Marks : {self.__marks}
        ''')

    def get_name(self):
        username = input("enter username: ")
        password = input("password: ")
        if username == "vaibhav" and password == "123":
            return self.__name

    def set_name(self, nm):
        if isinstance(nm, str) and nm.isalpha():
            self.__name = nm


s1 = Student("Vaibhav Patil", 26, 89)
s1.set_name('abc')
print(s1.details())