from mysql import connector

conn = connector.connect(
    user = "root",
    password = "9325",
    host = "localhost",
    port = "3306",
    database = "product_db"
)

print("connected...")

cur = conn.cursor()
pname = input("pname: ")
category = input("category: ")
cost_price = input("cost_price: ")
mrp = input("mrp: ")
cur.execute("INSERT INTO items (pname,category,cost_price,mrp) values(%s,%s,%s,%s)",
            (pname, category, cost_price, mrp))
conn.commit()
cur.close()
conn.close()


