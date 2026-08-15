from product import Product


class Electronics(Product):

    def __init__(self, product_id, product_name, category, price, supplier, warranty_years):
        super().__init__(product_id, product_name, category, price, supplier)
        self.warranty_years = warranty_years

    def calculate_final_price(self):
        discount = self.get_price() * 10 / 100
        final_price = self.get_price() - discount
        return final_price


    