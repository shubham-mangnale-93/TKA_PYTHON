# Calculate Total MRP, Total CP and Profit for Electronics Products:---->>

f = open("Day39 practice/products.txt", "r")

all_lines = f.readlines()

total_mrp = 0
total_cp = 0

for line in all_lines[1:]:
    data = line.strip("\n")
    data = data.split(",")

    if data[2] == "Electronics":
        mrp = int(data[3])
        cp = int(data[4])

        total_mrp = total_mrp + mrp
        total_cp = total_cp + cp

profit = total_mrp - total_cp

print("Electronics Total MRP:", total_mrp)
print("Electronics Total CP:", total_cp)
print("Electronics Profit:", profit)

f.close()