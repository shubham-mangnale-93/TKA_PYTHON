#open ??
# f = open("Day38 File And Exception/products.txt", "r")
#read:
# data = f.read()
# print(data)
#---------------------------------------------------------------------------

# read character:
# data = f.read(5)
# print(data)
#---------------------------------------------------------------------------

#readline:
# l1 = f.readline()
# print(l1)

# l2 = f.readline()
# print(l2)
#---------------------------------------------------------------------------

#readlines: Return a list of lines from the stream.
# lines = f.readlines()
# print(lines) # ['laptop 80000\n', 'mobile 30000\n', 'charger 2000\n', 'fan 3000\n']

#---------------------------------------------------------------------------

# mode w:
# f = open("Day38 File And Exception/products.txt", "w")
#write:
# f.write("TV 60000")  #overwrite first data.

#writes:
# f.writelines(['p1 40000\n','p2 10000\n','p3 5000'])
#---------------------------------------------------------------------------

#new file add:
# f = open("Day38 File And Exception/products123.txt", "w")
# f.write('p5 65000')
#---------------------------------------------------------------------------

# mode a: append
# f = open("Day38 File And Exception/products.txt", "a")
# f.write("\np4 65000")

# f = open("Day38 File And Exception/products345y.txt", "a")
# f.write("p4 65000")
#---------------------------------------------------------------------------

# # mode x:
f = open("Day38 File And Exception/products1256.txt", "x")
f.write("p4 65000")


