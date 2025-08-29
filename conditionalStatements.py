'''
a = int(input("Provide value A:\n"))
b = int(input("Provide value B:\n"))
c = int(input("Provide value C:\n"))

if a > b and a > c:
    print("A has the highest value")
elif b > a and b > c:
    print("B has the highest value")
elif c > a and c > b:
    print("C has the highest value")
else:
    print("There is no highest value // some are equal")
'''
'''
num1 = int(input("Please Enter an Integer: "))
num2 = int(input("Please Enter an Integer: "))

operator = input("Please Enter an Operator: ")

if operator == "+":
    print(f"The sum is {num1+num2}")
elif operator == "-":
    print(f"The difference is {num1-num2}")
elif operator == "*":
    print(f"The product is {num1*num2}")
elif operator == "/":
    print(f"The quotient is {float(num1/num2)}")
elif operator =="%":
    print(f"The remainder is {num1%num2}")
else:
    print("Please provide a correct operator.")
'''

StudentName = input("Please Enter Student Name:\n")
CourseCount = int(input("Please Enter number of courses:\n"))
GradeTotal = 0
for i in range(CourseCount):
    Grade = int(input(f"Please enter grade for course {(i+1)}:\n"))
    GradeTotal+=Grade
print(f'Grade Total = {GradeTotal}')
GradeAVG = float(GradeTotal/CourseCount)
print(f"{StudentName}'s Grade AVG = {GradeAVG}%")
if GradeAVG >= 90:
    print("Grade A")
elif GradeAVG < 90 and GradeAVG >= 80:
    print('Grade B')
elif GradeAVG < 80 and GradeAVG >= 70:
    print('Grade C')
elif GradeAVG < 70 and GradeAVG >= 60:
    print('Grade D')
else:
    print('Grade F')
