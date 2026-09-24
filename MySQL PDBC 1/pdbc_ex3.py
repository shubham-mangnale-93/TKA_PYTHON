# WAP to access using pid:-------------->>
from mysql import connector

conn = connector.connect(
    user='root',
    password='9325',
    host='localhost',
    port=3306,
    database = "product_db"
)
print("connected...")
# id = int(input("Enter PID: "))
# cur = conn.cursor()
# query = "select * from items where pid = %s"
# cur.execute(query,(id,))
# for i in cur:
#     print(i)


# F-String:
cur = conn.cursor()
id = int(input("Enter PID: "))
cur.execute(f"select * from items where pid = {id}")
for i in cur:
    print(i)


# Add new record - using F-String
pname = input("pname: ")
category = input("category: ")
cost_price = float(input("cost_price: "))
mrp = float(input("mrp: "))

cur.execute(f"insert into items (pname, category, cost_price, mrp) values ('{pname}', '{category}', {cost_price}, {mrp})")
conn.commit()
print("Record added successfully!")

cur.close()
conn.close()
