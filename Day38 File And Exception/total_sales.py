file = open("Day38 File And Exception/product_sale.txt", "r")
# data = file.readlines()
# total = 0
# for line in data:
#     line = line.strip("\n")
#     list = line.split()
#     sales_amount = float(list[1])
#     total = total + sales_amount

# print(total)
#---------------------------------------------------------------------------------
# method 2 : short way
data = file.readlines()
total = 0
for line in data:
    sales_amount = float(line.strip("\n").split()[1])
    total += sales_amount
print(total)

