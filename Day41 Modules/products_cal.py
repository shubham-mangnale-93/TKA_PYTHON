# import csv
# file = open("Day41 Modules/products_sales.csv","r")
# data = csv.reader(file)
# print(data)
# for record in data:
#     print(record)
#---------------------------------------------------------------------------------------------------

# import csv  
# file = open("Day41 Modules/student_data.csv","w")
# wr = csv.writer(file)
# # wr.writerow([1, "vaibhav", 89])  # write single line

# wr.writerow(["id", "name", "marks"])   #header
# wr.writerows([
#     [1, "vaibhav", 89],
#     [2, "rahul", 78],
#     [3, "amit", 85]
# ])
#---------------------------------------------------------------------------------------------------


# import csv
# file = open("Day41 Modules/products_sales.csv","r")
# reader = csv.reader(file)
# all_products = list(reader)
# print(all_products)
# total_cost_price = 0
# for record in all_products[1:]:
#     cp = record[-1]
#     print(cp)
#     total_cost_price += float(cp)
# print(total_cost_price)
#---------------------------------------------------------------------------------------------------

# import csv
# file = open("Day41 Modules/products_sales.csv", "r")
# all_records = csv.DictReader(file)

# for record in all_records:
#     print(record['cp'])
#---------------------------------------------------------------------------------------------------

# import csv   
# file = open("Day41 Modules/students_data.csv", "w")
# filds = ["roll", "name", "marks"]              # column headers
# writer = csv.DictWriter(file, fieldnames=filds)  # create a dict-based CSV writer
# writer.writeheader()                             # writes: roll,name,marks
# writer.writerow({"roll": 1, "name": "jay", "marks": 88})  # writes one row
#---------------------------------------------------------------------------------------------------

# import csv
# file = open("Day41 Modules/products_sales.csv", "r")
# all_records = csv.DictReader(file)

# for record in all_records:
#     profit = int(record["mrp"]) - int(record["cp"])   
#     print(record["pname"], "=", profit)

# file.close()
#---------------------------------------------------------------------------------------------------

# import csv
# file = open("Day41 Modules/products_sales.csv", "r")
# all_records = csv.DictReader(file)

# new_file = open("Day41 Modules/product_profit.csv", "w", newline="")
# writer = csv.writer(new_file)
# writer.writerow(["pname", "profit"])

# for record in all_records:
#     profit = int(record["mrp"]) - int(record["cp"])
#     writer.writerow([record["pname"], profit])

# file.close()
# new_file.close()

#---------------------------------------------------------------------------------------------------

import csv
file = open("Day41 Modules/products_sales.csv", "r")
p_file = open("Day41 Modules/profit.csv", "w")            # open new file for writing

writer = csv.DictWriter(p_file, fieldnames=['pid', 'pname', 'profit'])
writer.writeheader()                        # writes: pid,pname,profit

all_products = csv.DictReader(file)         # read source file as dicts

for product in all_products:
    pid = product["pid"]
    pname = product["pname"]
    mrp = float(product['mrp'])             # convert string -> float
    cp = float(product['cp'])       # convert string -> float
    profit = mrp - cp                       # calculate profit
    writer.writerow({'pid': pid, 'pname': pname, 'profit': profit})


