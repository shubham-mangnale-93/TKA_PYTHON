f = open("products.txt","w+")
print(f.readable())   # True
print(f.writable())   # True
#--------------------------------------------------

# r+ (read + write)
f = open("products.txt", "r+")
print(f.readable())   # True
print(f.writable())   # True
#--------------------------------------------------

# a+ (append + read)
f = open("products.txt", "a+")
print(f.readable())   # True
print(f.writable())   # True
#--------------------------------------------------

# x+ (exclusive create + read/write)
f = open("products.txt", "x+")
print(f.readable())   # True
print(f.writable())   # True

#--------------------------------------------------

