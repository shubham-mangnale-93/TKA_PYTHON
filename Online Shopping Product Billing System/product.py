class Product:

    def __init__(self, product_id, product_name, category, price, supplier):
        self.product_id = product_id
        self.product_name = product_name
        self.category = category
        self.__price = price
        self.supplier = supplier

    def get_price(self):
        return self.__price

    def set_price(self, price):

        if price >= 100:
            self.__price = price
        else:
            print("Price cannot be less than 100")

    def calculate_final_price(self):
        return self.__price

    def display(self):
        print("Product ID:", self.product_id)
        print("Product Name:", self.product_name)
        print("Category:", self.category)
        print("Price:", self.__price)
         
    def __str__(self):
        return f"{self.product_id} - {self.product_name} - {self.category}"

