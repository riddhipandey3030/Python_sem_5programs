#Create a dictonary Employee where employee id is the key,the value against employee id is the
# nested dictionary that includes emp_name,designation,department and salary.The dictionary contains
# records of 5 employees.Perform the following operations on the dictionary employee:
#1. Print the record of employee with emp_id E1
#2. Print the department of employee e4
#3. Print the record of employee having maximum salary
#4. Insert a new wmployee record in the existing dictionary
#------------------------------------------------------------------------------------------------

employee = {"E1": {"name": "Rahul","designation": "Manager","department": "HR","salary": 50000},
"E2": {"name": "Priya","designation": "Developer","department": "IT","salary": 60000},
"E3": {"name": "Amit","designation": "Tester","department": "IT","salary": 45000},
"E4": {"name": "Sneha","designation": "Analyst","department": "Finance","salary": 55000},
"E5": {"name": "Rohan","designation": "Manager","department": "Sales","salary": 70000}}

# 1. Print the record of employee E1
print("Record of Employee E1:")
print(employee["E1"])

# 2. Print the department of employee E4
print("\nDepartment of E4:")
print(employee["E4"]["department"])

# 3. Print the record of employee having maximum salary
max_employee = max(employee, key=lambda x: employee[x]["salary"])

print("\nEmployee with maximum salary:")
print(max_employee, employee[max_employee])

# 4. Insert a new employee record
employee["E6"] = {"name": "Neha","designation": "Developer","department": "IT","salary": 65000}
print("\nDictionary after inserting new employee:")
print(employee)