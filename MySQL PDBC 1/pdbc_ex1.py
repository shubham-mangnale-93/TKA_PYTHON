from mysql import connector

conn = connector.connect(
    user='root',
    password='9325',
    host='localhost',
    port=3306,
    database = "product_db"
)
print("connected...")

# cur = conn.cursor()
# cur.execute("select * from items")

# for i in cur:
#     print(i)

# cur = conn.cursor()
# cur.execute("show databases")

# for i in cur:
#     print(i)

# cur = conn.cursor()
# cur.execute("INSERT INTO items (pname, category, cost_price, mrp) VALUES "
# "('Mobile Phone', 'Electronics', 15000, 20000)")

# conn.commit()
# cur.close()
# conn.close()


