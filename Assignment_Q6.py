#Define a dictionary Student where roll no. is the key and value is another dictionary consisting 
# of name,department and marks.The student dictionary have recordds of 5 students.
# Use the lambda function to perform the following task.
# 1. Sort the dictionary according to the marks highest to lowest
# 2. Print the records of the student who scored maximum marks
# 3. Find the average marks of the student
# 4. Print the records of the students who score more than average marks
#--------------------------------------------------------------------------------------------

# Student dictionary
Student = {101: {"name": "Rahul","department": "CSE","marks": 85},102: {"name": "Priya","department": "AIML","marks": 92},
103: {"name": "Amit","department": "CSE","marks": 76},104: {"name": "Sneha","department": "AIML","marks": 88},
105: {"name": "Rohan","department": "CSE","marks": 69}}

# 1. Sort dictionary according to marks from highest to lowest
sorted_students = dict(sorted(Student.items(),key=lambda x: x[1]["marks"],reverse=True))
print("Students sorted according to marks:")
print(sorted_students)
# 2. Print record of student with maximum marks
max_student = max(Student,key=lambda x: Student[x]["marks"])
print("\nStudent with maximum marks:")
print(max_student, Student[max_student])
# 3. Find average marks
total = sum(Student[x]["marks"] for x in Student)
average = total / len(Student)
print("\nAverage marks:", average)
# 4. Print students who scored more than average marks
print("\nStudents scoring more than average marks:")
for roll_no, details in Student.items():
    if details["marks"] > average:
        print(roll_no, details)