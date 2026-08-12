class Cls_name():

    # Class attribute
    ca2 = "value2"

    def __init__(self):       # Initialization
        # Instance attribute
        self.ia1 = "value1"

    # Instance method
    def im1(self):
        print(self.ia1)

    # Class method
    @classmethod
    def cm1(cls):
        print(cls.ca2)

    # Static method
    @staticmethod
    def sm1():
        pass


obj = Cls_name()

# obj.im1()
# obj.cm1()

obj.sm1()