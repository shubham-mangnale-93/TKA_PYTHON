# Import Employee class
from employee import Employee

# Developer class inherits Employee
class Developer(Employee):

    # constructor 
    def __init__(self, employee_id, name, department, basic_salary, address, technology):

        # call Employee constructor
        super().__init__(employee_id, name, department, basic_salary, address)

        # store developer technology
        self.technology = technology

    # Override calculate_salary method
    def calculate_salary(self):

        # Add 5000 bonus to basic salary
        return self.get_salary() + 5000

    # Display Developer details
    def display(self):

        # Display employee information using __str__()
        print(self)

        # Display basic salary
        print("Basic Salary:", self.get_salary())

        # Display Developer bonus
        print("Bonus:", 5000)

        # Display final salary
        print("Final Salary:", self.calculate_salary())

        # Display technology
        print("Technology:", self.technology)

        # Display city
        print("City:", self.address.city)


    