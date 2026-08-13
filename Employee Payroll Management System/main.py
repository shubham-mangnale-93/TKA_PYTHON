# Import Address class
from address import Address

# Import Employee class
from employee import Employee

# Import Developer class
from developer import Developer

# Import Tester class
from tester import Tester

# Import Manager class
from manager import Manager
#-----------------------------------------------------------------------

# Create Address object
address1 = Address("Pune", "Maharashtra", 411001)


# Create Employee object
employee1 = Employee(
    101,
    "Rahul",
    "Development",
    40000,
    address1
)

# Create Developer object
developer1 = Developer(
    101,
    "Rahul",
    "Development",
    40000,
    address1,
    "Python"
)

# Create Address object for Tester
address2 = Address("Mumbai", "Maharashtra", 400001)


# Create Tester object
tester1 = Tester(
    102,
    "Priya",
    "Testing",
    35000,
    address2,
    "Automation"
)

# Create Address object for Manager
address3 = Address("Pune", "Maharashtra", 411002)


# Create Manager object
manager1 = Manager(
    103,
    "Amit",
    "Management",
    60000,
    address3,
    8
)
#-----------------------------------------------------------------------------------
# Display employee details
employee1.display()
print()
# Print employee object
print(employee1)

# Get employee salary
print(employee1.get_salary())


# Change employee salary
employee1.set_salary(50000)

# Display updated salary
print(employee1.get_salary())

# Try to set salary below 10000
employee1.set_salary(5000)

print("--"*30)
print("--"*30)
#-------------------------------------------------------------------------
# Calculate Developer salary
print(developer1.calculate_salary())

print(developer1.name)
print(developer1.technology)
print(developer1.get_salary())
print(developer1.calculate_salary())

# Display Developer details
developer1.display()
print("--"*30)
#------------------------------------------------------------------------- 

# Display Tester details
tester1.display()
print("--"*30)

#------------------------------------------------------------------------- 
# Display Manager details
manager1.display()
print("--"*30)

#------------------------------------------------------------------------- 

# Calculate Developer salary
print(developer1.calculate_salary())

# Calculate Tester salary
print(tester1.calculate_salary())

# Calculate Manager salary
print(manager1.calculate_salary())


# Store different employee objects in a list
employees = [developer1, tester1, manager1]

# Call the same method for every object
for employee in employees:
    print(employee.calculate_salary())