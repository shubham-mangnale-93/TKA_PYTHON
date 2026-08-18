file = open("Day39 practice/products.txt", "r")

data = file.readlines()

header = data[0]


# Create category files and write header

f = open("Day39 practice/Electronics.txt", "w")
f.write(header)
f.close()

f = open("Day39 practice/Clothing.txt", "w")
f.write(header)
f.close()

f = open("Day39 practice/Grocery.txt", "w")
f.write(header)
f.close()

f = open("Day39 practice/Stationery.txt", "w")
f.write(header)
f.close()


# Separate products category-wise

for line in data[1:]:

    line = line.strip("\n")
    line = line.split(",")

    category = line[2]

    if category == "Electronics":

        f = open("Day39 practice/Electronics.txt", "a")
        f.write(",".join(line) + "\n")
        f.close()

    elif category == "Clothing":

        f = open("Day39 practice/Clothing.txt", "a")
        f.write(",".join(line) + "\n")
        f.close()

    elif category == "Grocery":

        f = open("Day39 practice/Grocery.txt", "a")
        f.write(",".join(line) + "\n")
        f.close()

    elif category == "Stationery":

        f = open("Day39 practice/Stationery.txt", "a")
        f.write(",".join(line) + "\n")
        f.close()


file.close()