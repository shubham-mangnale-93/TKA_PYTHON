from mysql import connector

conn = connector.connect(
    host = "localhost",
    user = "root",
    password = "9325",
    database = "pdbc_db"
)
print("Connect_DB....")
cursor = conn.cursor()

def add_employee():
    emp_id = int(input("Enter Employee ID: "))
    emp_name = input("Enter Employee Name: ")
    department = input("Enter Department: ")
    salary = float(input("Enter Salary: "))
    joining_date = input("Enter Joining Date (YYY-MM-DD): ")

    query = "INSERT INTO emp (emp_id, emp_name, department, salary, joining_date) VALUES (%s, %s, %s, %s, %s)"
    values = (emp_id, emp_name, department, salary, joining_date)

    cursor.execute(query,values)
    conn.commit()
    print("EMP added successfully")
 

def update_employee():
    emp_id = int(input("Enter Employee ID to update: "))
    
    cursor.execute("SELECT * FROM emp WHERE emp_id = %s", (emp_id,))
    result = cursor.fetchone()
    
    if result is None:
        print("No employee found with this ID.")
        return
    
    print(f"Current Details -> Name: {result[1]}, Department: {result[2]}, Salary: {result[3]}")
    
    emp_name = input("Enter new Name: ")
    department = input("Enter new Department: ")
    salary = float(input("Enter new Salary: "))
    
    query = "UPDATE emp SET emp_name = %s, department = %s, salary = %s WHERE emp_id = %s"
    values = (emp_name, department, salary, emp_id)
    
    cursor.execute(query, values)
    conn.commit()
    print("Employee updated successfully!")

def delete_employee():
    emp_id = int(input("Enter Employee ID to delete: "))
    
    query = "DELETE FROM emp WHERE emp_id = %s"
    cursor.execute(query, (emp_id,))
    conn.commit()
    
    if cursor.rowcount == 0:
        print("No employee found with this ID.")
    else:
        print("Employee deleted successfully!")

def salary_increment():
    emp_id = int(input("Enter Employee ID: "))
    percent = float(input("Enter increment percentage: "))

    cursor.execute("SELECT salary FROM emp WHERE emp_id = %s", (emp_id,))
    result = cursor.fetchone()

    if result is None:
        print("No employee found with this ID.")
        return

    old_salary = float(result[0])
    new_salary = old_salary + (old_salary * percent / 100)

    cursor.execute("UPDATE emp SET salary = %s WHERE emp_id = %s", (new_salary, emp_id))
    conn.commit()
    print(f"Salary updated from {old_salary} to {new_salary}")

def give_bonus():
    emp_id = int(input("Enter Employee ID: "))

    cursor.execute("SELECT salary FROM emp WHERE emp_id = %s", (emp_id,))
    result = cursor.fetchone()

    if result is None:
        print("No employee found with this ID.")
        return

    salary = float(result[0])

    choice = input("Enter bonus as (1) Amount or (2) Percentage: ")

    if choice == "1":
        bonus = float(input("Enter bonus amount: "))
    else:
        bonus_percent = float(input("Enter bonus percentage: "))
        bonus = salary * bonus_percent / 100

    new_salary = salary + bonus

    cursor.execute("UPDATE emp SET salary = %s WHERE emp_id = %s", (new_salary, emp_id))
    conn.commit()
    print(f"Bonus of {bonus} given. New salary: {new_salary}")


def search_employee():
    choice = input("Search by (1) Employee ID or (2) Employee Name: ")

    if choice == "1":
        emp_id = int(input("Enter Employee ID: "))
        cursor.execute("SELECT * FROM emp WHERE emp_id = %s", (emp_id,))
    else:
        emp_name = input("Enter Employee Name: ")
        cursor.execute("SELECT * FROM emp WHERE emp_name = %s", (emp_name,))

    results = cursor.fetchall()

    if not results:
        print("No employee found.")
    else:
        for result in results:
            print(f"ID: {result[0]}, Name: {result[1]}, Department: {result[2]}, Salary: {result[3]}, Joining Date: {result[4]}")

def display_all_employees():
    cursor.execute("SELECT * FROM emp")
    results = cursor.fetchall()

    print(f"{'ID':<6}{'Name':<12}{'Department':<12}{'Salary':<10}{'Joining Date':<15}")
    for row in results:
        print(f"{row[0]:<6}{row[1]:<12}{row[2]:<12}{row[3]:<10}{str(row[4]):<15}")

while True:
    print("\n========== Employee Management System ==========")
    print("1. Add New Employee")
    print("2. Update Employee Details")
    print("3. Delete Employee")
    print("4. Give Salary Increment")
    print("5. Give Bonus")
    print("6. Search Employee")
    print("7. Display All Employees")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_employee()
    elif choice == "2":
        update_employee()
    elif choice == "3":
        delete_employee()
    elif choice == "4":
        salary_increment()
    elif choice == "5":
        give_bonus()
    elif choice == "6":
        search_employee()
    elif choice == "7":
        display_all_employees()
    elif choice == "8":
        print("Exiting the system. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

cursor.close()
conn.close()

