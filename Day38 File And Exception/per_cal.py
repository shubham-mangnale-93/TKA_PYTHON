f = open("Day38 File And Exception/shubham_marks.txt", "r")
all_lines = f.readlines()
obt_mk = 0
no_sub = 0
for line in all_lines:
    # print(line)
    line = line.strip("\n")
    list = line.split() #Return a list of the substrings in the string, using sep as the separator string.
    marks = float(list[1])
    obt_mk = obt_mk + marks
    no_sub = no_sub + 1

print(obt_mk)
# print(no_sub)
total_mk = no_sub * 100
per = obt_mk/total_mk * 100
print(per)

#-----------------------------------------------------------------------------------------------------



