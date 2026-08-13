# PYTHON OOP PRACTICAL TASK:-------------->>>>>>>
'''
1. Employee Class
• Attributes: employee_id, name, department, __basic_salary, address.
• Use __init__() to initialize the data.
• Keep __basic_salary private.
• Create methods: get_salary(), set_salary(), calculate_salary(), display().
• Business Rule: Basic salary cannot be less than Rs. 10,000.
'''
class Employee:

    def __init__(self, employee_id, name, department, basic_salary, address):
        self.employee_id = employee_id
        self.name = name
        self.department = department
        self.__basic_salary = basic_salary   # private attribute
        self.address = address

    










