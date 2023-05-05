# Import the necessary functions and modules
from employee_info import get_employees_by_age_range, calculate_average_salary, get_employees_by_dept


# Define the test cases for get_employees_by_age_range
def test_get_employees_by_age_range():
    # Test Case 1: age_lower_limit = 25, age_upper_limit = 30
    assert get_employees_by_age_range(25, 30) == [{"name": "John", "age": 30, "department": "Sales", "salary": 50000},
                                                  {"name": "Jane", "age": 25, "department": "Marketing",
                                                   "salary": 60000}]

    # Test Case 2: age_lower_limit = 30, age_upper_limit = 40
    assert get_employees_by_age_range(30, 40) == [{"name": "John", "age": 30, "department": "Sales", "salary": 50000},
                                                  {"name": "Chloe", "age": 35, "department": "Engineering",
                                                   "salary": 70000},
                                                  {"name": "Mike", "age": 32, "department": "Engineering",
                                                   "salary": 65000},
                                                  {"name": "Peter", "age": 40, "department": "Sales", "salary": 60000}]

    # Test Case 3: age_lower_limit = 22, age_upper_limit = 23
    assert get_employees_by_age_range(22, 23) == [
        {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000}]


# Define the test cases for calculate_average_salary
def test_calculate_average_salary():
    # Test Case 1
    assert calculate_average_salary() ==60166.666666666664

    # Test Case 2: Add a new employee to the employee_data list
    employee_data = [
        {"name": "John", "age": 30, "department": "Sales", "salary": 50000},
        {"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
        {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000},
        {"name": "Chloe", "age": 35, "department": "Engineering", "salary": 70000},
        {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000},
        {"name": "Peter", "age": 40, "department": "Sales", "salary": 60000},
        {"name": "Bob", "age": 45, "department": "Marketing", "salary": 55000}  # new employee
    ]
    assert calculate_average_salary() == 60166.666666666664


# Define the test cases for get_employees_by_dept
def test_get_employees_by_dept():
    # Test Case 1: department = 'Sales'
    assert get_employees_by_dept('Sales') == [{'name': 'John', 'age': 30, 'department': 'Sales', 'salary': 50000},
                                              {'name': 'Peter', 'age': 40, 'department': 'Sales', 'salary': 60000}]

    # Test Case 2: department = 'Engineering'
    assert get_employees_by_dept("Engineering") == [{'name': 'Chloe', 'age': 35, 'department': 'Engineering', 'salary': 70000}, {'name': 'Mike', 'age': 32, 'department': 'Engineering', 'salary': 65000}]
    # Test Case 3: department = 'Marketing'
    assert get_employees_by_dept("Marketing") == [{'name': 'Jane', 'age': 25, 'department': 'Marketing', 'salary': 60000}, {'name': 'Mary', 'age': 23, 'department': 'Marketing', 'salary': 56000}]
