file = open("Day38 File And Exception/course_sales.txt", "r")

# WAP to cal WB total sales amount:---->>
# all_lines = file.readlines()
# total = 0
# for line in all_lines:
#     #  print(line)
#      line = line.strip("\n")
#      data = line.split()

#      if data[1] == "WD":
#           sales = int(data[2])
#           total = total + sales
# print("WD Total Sales:", total)          
#-------------------------------------------------------------------

# WAP to cal DA + DS = total sales:----->>
# all_lines = file.readlines()
# total = 0
# for line in all_lines:
#     #  print(line)
#      line = line.strip("\n")
#      data = line.split()

#      if data[1] == "DA" or data[1]== "DS":
#           sales = int(data[2])
#           total = total + sales
# print("DA + DS Total Sales:", total)          

# #---------------------------------------------------------------------

# # WAP to cal march month total sales:-------->>
# all_lines = file.readlines()
# total = 0
# for line in all_lines:
#     #  print(line)
#      line = line.strip("\n")
#      data = line.split()

#      if data[0] == "Mar":
#           sales = int(data[2])
#           total = total + sales
# print("March Total Sales:", total)    
#---------------------------------------------------------------------

# Calculate and find the month with the highest sales:----->>

# all_lines = file.readlines()

# Jan = 0
# Feb = 0
# Mar = 0

# for line in all_lines:    
#      line = line.strip("\n")
#      data = line.split()
#      month = data[0]
#      sales = int(data[2])

#      if month == "Jan":
#           Jan += sales
#      elif month == "Feb":
#           Feb += sales
#      elif month == "Mar":
#           Mar += sales

# if Jan > Feb and Jan > Mar:
#      print("Highest Sales: January", Jan)
# elif Feb > Jan and Feb > Mar:
#      print("Highest Sales: February", Feb)
# else:
#      print("Highest Sales: March", Mar)
      
#-----------------------------------------------------------------------

# calculate and find the department with the highest sales:-------->>>

# all_lines = file.readlines()

# DA = 0
# DS = 0
# WD = 0

# for line in all_lines:    
#      line = line.strip("\n")
#      data = line.split()
#      department = data[1]
#      sales = int(data[2])

#      if department == "DA":
#           DA += sales
#      elif department == "DS":
#           DS += sales
#      elif department == "WD":
#           WD += sales

# if DA > DS and DA > WD:
#      print("Highest Sales: DA", DA)
# elif DS > DA and DS > WD:
#      print("Highest Sales: DS", DS)
# else:
#      print("Highest Sales: WD", WD)
#-----------------------------------------------------------------------
      
# Find the sales of DA Department in February:
all_lines = file.readlines()

for line in all_lines:
    line = line.strip("\n")
    data = line.split()

    if data[0] == "Feb" and data[1] == "DA":
        print("February DA Sales:", data[2])
        

