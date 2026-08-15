from product import Product


class Clothing(Product):
    def __init__(self, product_id, product_name, category, price, supplier, size):
        super().__init__(product_id, product_name, category, price, supplier)
        self.size = size

    def calculate_final_price(self):
        discount = self.get_price() * 20 / 100
        final_price = self.get_price() - discount
        return final_price


