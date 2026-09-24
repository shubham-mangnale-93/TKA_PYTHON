import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="9325",
    database="pdbc_db"
)
print ("connect...")
'''
# Task 1 - Salary Category
# Fetch all employees using Python + MySQL.
# Salary >= 50,000 -> "High Salary"
# Salary >= 40,000 -> "Medium Salary"
# Otherwise -> "Low Salary"
# Display employee name, salary and salary category.
'''
# cursor = conn.cursor()
# cursor.execute("SELECT * FROM employees")
# results = cursor.fetchall()
 
# for result in results:
#     salary = result[-1]
#     emp_name = result[1]
#     if salary >= 50000:
#         category = "High Salary"
#     elif salary >= 40000:
#         category = "Medium Salary"
#     else:
#         category = "Low Salary"
    
#     print(f"Name: {emp_name} | Salary: {salary} | Category: {category}")
#-----------------------------------------------------------------------------------------------

'''
Task 2 - Bonus Calculation
Fetch all employees.
Using Python:
IT employees -> 15% bonus
Sales employees -> 10% bonus
HR employees -> 8% bonus
Calculate and display bonus amount and final salary.
'''
# METHOD 1:----------------------------------->>
# cursor = conn.cursor()
# cursor.execute("SELECT * FROM employees")
# results = cursor.fetchall()

# print(f"{'Emp_Name':<10}{'Department':<12}{'Salary':<10}{'Bonus':<10}{'Final Salary':<15}")

# for result in results:
#     emp_name = result[1]
#     department = result[2]
#     salary = float(result[-1])
#     if department == "IT":
#         bonus_percent = 0.15
#     elif department == "Sales":
#         bonus_percent = 0.10
#     elif department == "HR":
#         bonus_percent = 0.08
#     else:
#         bonus_percent = 0

#     bonus_amount = salary * bonus_percent
#     final_salary = salary + bonus_amount

#     print(f"{emp_name:<10}{department:<12}{salary:<10}{bonus_amount:<10}{final_salary:<15}")

# METHOD 2:----------------------------------->>
# cur = conn.cursor(dictionary=True)
# cur.execute("select * from employees")
# all_records = cur.fetchall()

# for record in all_records:
#     name = record['emp_name']
#     sal = record['salary']
#     dep = record['department']
    
#     if dep == "IT":
#         bonus = sal * 15/100
#     elif dep == "Sales":
#         bonus = sal * 10/100
#     elif dep == "HR":
#         bonus = sal * 8/100
    
#     final_sal = sal + bonus
#     print(name, bonus, final_sal)

#-----------------------------------------------------------------------------------------------

'''
Task 3 - Employee Tax Calculation
Fetch employees whose salary is greater than 40,000.
Using Python:
Salary >= 50,000 -> 10% tax
Salary < 50,000 -> 5% tax
Display employee name, salary, tax and salary after tax.
'''

#METHOD 1:----------------------------------------------->>
# cur = conn.cursor(dictionary=True)
# cur.execute("select * from employees where salary > 40000")
# all_records = cur.fetchall()

# print(f"{'Name':<10}{'Salary':<10}{'Tax':<10}{'Salary After Tax':<18}")

# for record in all_records:
#     name = record['emp_name']
#     sal = float(record['salary'])
    
#     if sal >= 50000:
#         tax = sal * 10/100
#     else:
#         tax = sal * 5/100    
#     salary_after_tax = sal - tax
    
#     print(f"{name:<10}{sal:<10}{tax:<10}{salary_after_tax:<18}")


#METHOD 2:-------------------->>
# cursor = conn.cursor()

# cursor.execute("SELECT * FROM employees WHERE salary > 40000")
# results = cursor.fetchall()

# print(f"{'Name':<10}{'Salary':<10}{'Tax':<10}{'Salary After Tax':<18}")

# for result in results:
#     emp_name = result[1]
#     salary = float(result[-1])
    
#     if salary >= 50000:
#         tax = salary * 10/100
#     else:
#         tax = salary * 5/100   
#     salary_after_tax = salary - tax
    
#     print(f"{emp_name:<10}{salary:<10}{tax:<10}{salary_after_tax:<18}")
#-----------------------------------------------------------------------------------------------

'''
Task 4 - Performance Bonus
Fetch all employees.
Assume performance score using Python:
IT -> 90
Sales -> 80
HR -> 75
Calculate bonus:
Score >= 90 -> 15% bonus
Score >= 80 -> 10% bonus
Otherwise -> 5% bonus
Display employee name, department, score and bonus.
'''

# cursor = conn.cursor()

# cursor.execute("SELECT * FROM employees")
# results = cursor.fetchall()

# print(f"{'Name':<10}{'Department':<12}{'Score':<8}{'Bonus':<10}")

# for result in results:
#     emp_name = result[1]
#     department = result[2]
#     salary = float(result[-1])
    
#     if department == "IT":
#         score = 90
#     elif department == "Sales":
#         score = 80
#     elif department == "HR":
#         score = 75
#     else:
#         score = 0
    
#     if score >= 90:
#         bonus = salary * 15/100
#     elif score >= 80:
#         bonus = salary * 10/100
#     else:
#         bonus = salary * 5/100
    
#     print(f"{emp_name:<10}{department:<12}{score:<8}{bonus:<10}")
#-----------------------------------------------------------------------------------------------

'''
Task 5 - Insert Calculated Data
Create table: employee_summary (emp_id, emp_name, department, salary, bonus, final_salary)
Fetch employees from employees table and calculate:
Salary >= 50,000 -> 10% bonus
Salary < 50,000 -> 5% bonus
Then insert the calculated result into employee_summary using Python.
'''

# cursor = conn.cursor()

# cursor.execute("SELECT * FROM employees")
# results = cursor.fetchall()

# for result in results:
#     emp_id = result[0]
#     emp_name = result[1]
#     department = result[2]
#     salary = float(result[-1])
    
#     if salary >= 50000:
#         bonus = salary * 10/100
#     else:
#         bonus = salary * 5/100
    
#     final_salary = salary + bonus
    
#     insert_query = "INSERT INTO emp_summary (emp_id, emp_name, department, salary, bonus, final_salary) VALUES (%s, %s, %s, %s, %s, %s)"
#     values = (emp_id, emp_name, department, salary, bonus, final_salary)
    
#     cursor.execute(insert_query, values)

# conn.commit()

# print("Data inserted successfully into employee_summary")
#-----------------------------------------------------------------------------------------------


'''
Task 6 - Department-wise Calculation
Fetch all employee records.
Using Python, calculate:
Total salary of IT employees
Total salary of HR employees
Total salary of Sales employees
Average salary of each department
Do the calculations in Python, not using SQL aggregate functions.
'''

# cursor = conn.cursor()

# cursor.execute("SELECT * FROM employees")
# results = cursor.fetchall()

# it_total = 0
# it_count = 0
# sales_total = 0
# sales_count = 0
# hr_total = 0
# hr_count = 0

# for result in results:
#     department = result[2]
#     salary = float(result[-1])
    
#     if department == "IT":
#         it_total = it_total + salary
#         it_count = it_count + 1
#     elif department == "Sales":
#         sales_total = sales_total + salary
#         sales_count = sales_count + 1
#     elif department == "HR":
#         hr_total = hr_total + salary
#         hr_count = hr_count + 1

# it_average = it_total / it_count
# sales_average = sales_total / sales_count
# hr_average = hr_total / hr_count

# print("IT Department:")
# print(f"Total Salary: {it_total}")
# print(f"Average Salary: {it_average}")
# print()

# print("Sales Department:")
# print(f"Total Salary: {sales_total}")
# print(f"Average Salary: {sales_average}")
# print()

# print("HR Department:")
# print(f"Total Salary: {hr_total}")
# print(f"Average Salary: {hr_average}")

#-----------------------------------------------------------------------------------------------

'''
Task 7 - Employee Promotion
Fetch all employees.
Using Python:
Salary >= 50,000 -> "Eligible for Promotion"
Otherwise -> "Not Eligible"
Display employee name, salary and promotion status.
'''

# cursor = conn.cursor()

# cursor.execute("SELECT * FROM employees")
# results = cursor.fetchall()

# print(f"{'Name':<10}{'Salary':<10}{'Promotion Status':<25}")

# for result in results:
#     emp_name = result[1]
#     salary = float(result[-1])
    
#     if salary >= 50000:
#         status = "Eligible for Promotion"
#     else:
#         status = "Not Eligible"
    
#     print(f"{emp_name:<10}{salary:<10}{status:<25}")
#-----------------------------------------------------------------------------------------------

'''
Task 8 - Salary Increment + Database Update
Fetch all employees.
Using Python:
IT -> 12% increment
Sales -> 10% increment
HR -> 8% increment
Calculate the new salary and update the salary in MySQL using Python.
'''

# cursor = conn.cursor()

# cursor.execute("SELECT * FROM employees")
# results = cursor.fetchall()

# for result in results:
#     emp_id = result[0]
#     department = result[2]
#     salary = float(result[-1])
    
#     if department == "IT":
#         increment_percent = 12/100
#     elif department == "Sales":
#         increment_percent = 10/100
#     elif department == "HR":
#         increment_percent = 8/100
#     else:
#         increment_percent = 0
    
#     new_salary = salary + (salary * increment_percent)
    
#     update_query = "UPDATE employees SET salary = %s WHERE emp_id = %s"
#     values = (new_salary, emp_id)
    
#     cursor.execute(update_query, values)

# conn.commit()
# print("Salaries updated successfully")
#-----------------------------------------------------------------------------------------------

'''
Task 9 - Create New Records
Create table: employee_incentive (emp_id, emp_name, department, incentive)
Fetch employees and calculate:
Salary >= 50,000 -> Rs.5,000 incentive
Salary >= 40,000 -> Rs.3,000 incentive
Otherwise -> Rs.2,000 incentive
Insert the calculated incentive into the new table.
'''

# cursor = conn.cursor()

# cursor.execute("SELECT * FROM employees")
# results = cursor.fetchall()

# for result in results:
#     emp_id = result[0]
#     emp_name = result[1]
#     department = result[2]
#     salary = float(result[-1])
    
#     if salary >= 50000:
#         incentive = 5000
#     elif salary >= 40000:
#         incentive = 3000
#     else:
#         incentive = 2000
    
#     insert_query = "INSERT INTO employee_incentive (emp_id, emp_name, department, incentive) VALUES (%s, %s, %s, %s)"
#     values = (emp_id, emp_name, department, incentive)
    
#     cursor.execute(insert_query, values)

# conn.commit()
# print("Data inserted successfully into employee_incentive")
#-----------------------------------------------------------------------------------------------

'''
Task 10 - Find Highest & Lowest Salary
Fetch all employee records using fetchall().
Without using MAX() or MIN() in SQL, use Python logic to find:
Employee with highest salary
Employee with lowest salary
Difference between highest and lowest salary.
'''

cursor = conn.cursor()

cursor.execute("SELECT * FROM employees")
results = cursor.fetchall()

highest_salary = float(results[0][-1])
highest_emp = results[0][1]

lowest_salary = float(results[0][-1])
lowest_emp = results[0][1]

for result in results:
    emp_name = result[1]
    salary = float(result[-1])
    
    if salary > highest_salary:
        highest_salary = salary
        highest_emp = emp_name
    
    if salary < lowest_salary:
        lowest_salary = salary
        lowest_emp = emp_name

difference = highest_salary - lowest_salary

print(f"Highest Salary: {highest_emp} - {highest_salary}")
print(f"Lowest Salary: {lowest_emp} - {lowest_salary}")
print(f"Difference: {difference}")

cursor.close()
conn.close()





