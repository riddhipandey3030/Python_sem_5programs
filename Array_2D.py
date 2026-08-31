# Create a 2D array to store the marks of 3 subjects of 5 student.
# Perform the following operations on the marks array 
# Find the maximum marks 
# Find the minimum marks
# Find the average marks
# Find the student id (0-5) who scored maximum marks in sub1
# Find maximum marks subject wise 
# Find average marks subject wise
# Add 10 marks for all students who scored less than 50 in subject 1(2nd column)
# Find out number of students score more than 80 in subject 2 (count)
# Find out the minimum marks of student 2 
# Find out the maximum marks of student 4
#-----------------------------------------------------------------------------------------

import numpy as np
marks = np.array([[78, 85, 90],[88, 45, 95],[92, 89, 84],[65, 32, 70],[81, 49, 88]])
print("Marks Array:")
print(marks)
# 1. Find the maximum marks
print("\nMaximum marks:", np.max(marks))
# 2. Find the minimum marks
print("Minimum marks:", np.min(marks))
# 3. Find the average marks
print("Average marks:", np.mean(marks))
# 4. Find the student ID (0 to 5) who scored maximum marks in Subject 1
student_id = np.argmax(marks[:, 1])#take all rows and column 1 and find position/index of max value
print("Student ID who scored maximum marks in Subject 1:", student_id)
print("Maximum marks in Subject 1:", marks[student_id, 1])
# 5. Find maximum marks subject-wise
max_subject_wise = np.max(marks, axis=0) # gives column wise
print("Maximum marks subject-wise:", max_subject_wise)
# 6. Find average marks subject-wise
avg_subject_wise = np.mean(marks, axis=0)# calculate the avg of each column
print("Average marks subject-wise:", avg_subject_wise)
# 7. Add 10 marks for all student who scored less than 50 in subject 1
marks[marks[:, 1] < 50, 1] += 10 # Selects the 2nd column
print("\nMarks after adding 10 marks to students scoring less than 50 in Subject 1:")
print(marks)
# 8. Find the number of students who scored more than 80 in subject 2
count = np.sum(marks[:, 2] > 80)#select the 2nd column and check whether greater than 80 or not
print("\nThe number of students who scored more than 80 in subject 2: ")
print(count)
# 9. Find out the minimum marks of student 2 
print("Minimum marks of Student 2:", np.min(marks[2]))
# 10. Find out the maximum marks of student 4
print("Maximum marks of Student 4:", np.max(marks[4]))

