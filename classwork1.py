'''
Problem 1:

print('Welcome to OOP Class')
name = input('Please Enter your Name:\n')
print(f'Welcome {name}')

Problem 2 (Method 1):

c1 = int(input("Enter the grade for Course 1:\n"))
c2 = int(input("Enter the grade for Course 2:\n"))
c3 = int(input("Enter the grade for Course 3:\n"))
c4 = int(input("Enter the grade for Course 4:\n"))
c5 = int(input("Enter the grade for Course 5:\n"))

Total = c1+c2+c3+c4+c5
print(f'Grade Total = {Total}')
print('Grade Average = ', float((Total / 5)))

Problem 2 (Method 2):

StudentName = input("Please Enter Student Name:\n")
CourseCount = int(input("Please Enter number of courses:\n"))
GradeTotal = 0
for i in range(CourseCount):
    Grade = int(input(f"Please enter grade for course {(i+1)}:\n"))
    GradeTotal+=Grade
print(f'Grade Total = {GradeTotal}')
print(f"{StudentName}'s Grade AVG = {float(GradeTotal/CourseCount)}")
'''

#Problem 3:
Empname = input('Please enter Employee name:\n')

wages = int(input("Enter Employee wage ($/hr):\n"))
hours = int(input('Enter Employee hours per day:\n'))
days = int(input("Enter Employee days worked per month:\n"))

MonthlyWage = wages*hours*days

print(Empname, "makes ", MonthlyWage, '$/month')
