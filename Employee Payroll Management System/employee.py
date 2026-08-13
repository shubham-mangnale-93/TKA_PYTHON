# Employee Class
class Employee:

    # constructor
    def __init__(self,employee_id, name, department, basic_salary, address):

        # store- employee_id, name, department, basic_salary, address
        self.employee_id = employee_id
        self.name = name
        self.department = department
        self.__basic_salary = basic_salary
        self.address = address

    # get basic salary
    def get_salary(self):
        return self.__basic_salary

    # set basic salary
    def set_salary(self,salary):

         # salary must be at least 10000
         if salary >= 10000:
             self.__basic_salary = salary
         else:
             print("Basic salary cannot be less than Rs. 10,000")

    # calculate salary
    def Calculate_salary(self):
        return self.__basic_salary


    # Display employee details 
    def display(self):
        print("Employee ID:", self.employee_id)
        print("Name:", self.name)
        print("Department:", self.department)
        print("Basic Salary:", self.__basic_salary)
        print("City:", self.address.city)

    # Special method
    def __str__(self):
        # return employee information as a string
        return f'{self.employee_id} - {self.name} - {self.department}'   

  

            

            




