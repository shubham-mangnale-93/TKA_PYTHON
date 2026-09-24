from mysql import connector

conn = connector.connect(
    user='root',
    password='9325',
    host='localhost',
    port=3306,
    database='restaurant_db'
)
cur = conn.cursor()

def show_menu():
    cur.execute("SELECT * FROM menu")
    all_rows = cur.fetchall()
    for row in all_rows:
        print(f'{row[0]}. {row[1]}')

def add_new_items():
    item_name = input("Item Name: ")
    category = input("category: ")
    price = float(input("Price: "))
    query = "INSERT INTO menu(item_name,category,price) values (%s,%s,%s)"
    values = (item_name, category, price)
    cur.execute(query, values)
    conn.commit()

def update_price():
    id = int(input("Item Id: "))
    pr = eval(input("Price: "))
    cur.execute(f"UPDATE menu set price = {pr} where item_id = {id}")
    conn.commit()

def delete_item():
    id = int(input("Item Id: "))
    cur.execute(f"delete from menu where item_id = {id}")
    conn.commit()

def generate_bill():
    c_name = input("Enter Name: ")
    items = []
    total_amount = 0
    while True:
        show_menu()
        item_id = int(input("Enter Item ID: "))
        q = int(input("Enter Quantity: "))
        cur.execute(f"SELECT * from menu where item_id ={item_id}")
        item_data = cur.fetchone()
        item_name = item_data[1]
        price = item_data[-1]
        amount = q*price
        total_amount = total_amount+amount
        items.append((item_id,item_name,q,price,amount))
        ch = input("Do You want to continue (y/n): ")
        if ch == 'n':
            break
    print('-'*106)
    print(f'|{"Item Id":^20}|{"Item Name":^20}|{"Quantity":^20}|{"Price":^20}|{"Amount":^20}|')
    print('-'*106)
    for item in items:
        print(f'|{item[0]:^20}|{item[1]:^20}|{item[2]:^20}|{item[3]:^20}|{item[4]:^20}|')
    print('-'*106)
    print(f'Total Amount: {total_amount}')
    

 

