# Import the necessary functions and modules
import employee_info

# Define the test cases for get_employees_by_age_range
def test_get_employees_by_age_range():
    # Test Case 1: age_lower_limit = 25, age_upper_limit = 30
    expected = [{"name": "John", "age": 30, "department": "Sales", "salary": 50000},
                                                  {"name": "Jane", "age": 25, "department": "Marketing",
                                                   "salary": 60000}]
    result = employee_info.get_employees_by_age_range(25, 30)
    assert (result == expected)

def test_get_employees_by_age_range():

    # Test Case 2: age_lower_limit = 30, age_upper_limit = 40
    expected = [{"name": "John", "age": 30, "department": "Sales", "salary": 50000},
                                                  {"name": "Chloe", "age": 35, "department": "Engineering",
                                                   "salary": 70000},
                                                  {"name": "Mike", "age": 32, "department": "Engineering",
                                                   "salary": 65000},
                                                  {"name": "Peter", "age": 40, "department": "Sales", "salary": 60000}]
    result = employee_info.get_employees_by_age_range(30, 40)
    assert (result == expected)


# Define the test cases for calculate_average_salary
def test_calculate_average_salary():
    # Test Case 1
    expected =60166.666666666664
    result = employee_info.calculate_average_salary()
    assert (result == expected)

# Define the test cases for get_employees_by_dept
def test_get_employees_by_dept():
    # Test Case 1: department = 'Sales'
    expected = [{'name': 'John', 'age': 30, 'department': 'Sales', 'salary': 50000},
                                              {'name': 'Peter', 'age': 40, 'department': 'Sales', 'salary': 60000}]
    result = employee_info.get_employees_by_dept('Sales')
    assert (result == expected)

