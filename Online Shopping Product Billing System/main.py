from supplier import Supplier
from electronics import Electronics
from clothing import Clothing
from grocery import Grocery

# Supplier objects
supplier1 = Supplier("TechWorld", "Pune", "9876543210")
supplier2 = Supplier("FashionHub", "Mumbai", "9876543211")
supplier3 = Supplier("FreshMart", "Pune", "9876543212")

# Product objects
e1 = Electronics(
    "P101",
    "Laptop",
    "Electronics",
    50000,
    supplier1,
    2
)

c1 = Clothing(
    "P102",
    "Jacket",
    "Clothing",
    3000,
    supplier2,
    "L"
)

g1 = Grocery(
    "P103",
    "Rice Bag",
    "Grocery",
    2000,
    supplier3,
    "31-12-2026"
)

# Electronics
print("----- Electronics -----")
print(e1)
e1.display()
print("Warranty:", e1.warranty_years, "Years")
print("Final Price:", e1.calculate_final_price())

# Clothing
print("\n----- Clothing -----")
print(c1)
c1.display()
print("Size:", c1.size)
print("Final Price:", c1.calculate_final_price())

# Grocery
print("\n----- Grocery -----")
print(g1)
g1.display()
print("Expiry Date:", g1.expiry_date)
print("Final Price:", g1.calculate_final_price())


