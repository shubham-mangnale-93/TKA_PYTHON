# Import Employee class
from employee import Employee

# Manager class inherits Employee
class Manager(Employee):

    # Constructor
    def __init__(self, employee_id, name, department, basic_salary, address, team_size):

        # Call Employee constructor
        super().__init__(employee_id, name, department, basic_salary, address)

        # Store team size
        self.team_size = team_size

    # Override calculate_salary method
    def calculate_salary(self):

        # Add 10000 bonus to basic salary
        return self.get_salary() + 10000

    # Display Manager details
    def display(self):

        # Display employee information
        print(self)

        # Display basic salary
        print("Basic Salary:", self.get_salary())

        # Display Manager bonus
        print("Bonus:", 10000)

        # Display final salary
        print("Final Salary:", self.calculate_salary())

        # Display team size
        print("Team Size:", self.team_size)

        # Display city
        print("City:", self.address.city)

        