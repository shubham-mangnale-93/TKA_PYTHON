from product import Product

class Grocery(Product):

    def  __init__(self, product_id, product_name, category, price, supplier,  expiry_date):
        super().__init__(product_id, product_name, category, price, supplier)
        self. expiry_date =  expiry_date

    def calculate_final_price(self):
        discount = self.get_price() * 5 / 100
        final_price = self.get_price() - discount
        return final_price

    