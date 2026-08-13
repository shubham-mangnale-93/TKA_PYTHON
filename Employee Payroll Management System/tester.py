# Import Employee class
from employee import Employee

# Tester class inherits Employee
class Tester(Employee):

    def __init__(self, employee_id, name, department, basic_salary, address, testing_type):

        # call employee constructor
        super().__init__(employee_id, name, department, basic_salary, address)

        # store testing type
        self.testing_type = testing_type

    # Override calculate_salary method
    def calculate_salary(self):

        # Add 3000 bonus to basic salary
        return self.get_salary() + 3000  


    # Display Tester details
    def display(self):

        # Display employee information
        print(self)

        # Display basic salary
        print("Basic Salary:", self.get_salary())

        # Display Tester bonus
        print("Bonus:", 3000)

        # Display final salary
        print("Final Salary:", self.calculate_salary())

        # Display testing type
        print("Testing Type:", self.testing_type)

        # Display city
        print("City:", self.address.city)

         