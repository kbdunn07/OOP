'''
stu = \
    {
        's1': {'Name': 'Kyle', 'Major': 'CS', 'Year': 'Freshman', 'Credits': '15', 'GPA': '4.0'},
        's2': {'Name': 'John', 'Major': 'AI', 'Year': 'Junior', 'Credits': '17', 'GPA': '3.5'}
    }

for stuRec in stu.items():
    print(stuRec)
    print('-----------------------------------------------------------------------')
sid = input("Please provide student ID: ")
sname = input("Enter Student name: ")
smajor = input("Enter Student Major: ")
syear = input("Enter Student Year: ")
scredit = input("Enter Student Credit Hours: ")
sGPA = input("Enter Student GPA: ")

stu.update({sid:{'Name':sname, 'Major':smajor, 'Year':syear, 'Credit':scredit, 'GPA':sGPA}})

for stuRec in stu.items():
    print(stuRec)
    print('-----------------------------------------------------------------------')

'''
while True:
    stu = {}
    print('\n1. Add Student in the Dictionary\n'
          '2. Delete Student from the Dictionary\n'
          '3. Replace a Student in the Dictionary\n'
          '4. Print the Dictionary\n'
          '5. Quit\n')
    choice = input("Please enter your choice: ")
    if choice=="1":
        sid = input("Enter Student ID: ")
        sname = input("Enter Student Name: ")
        smajor = input('Enter Student Major: ')
        syear = input('Enter Student Year: ')
        scredit = input('Enter Student Credit Hours: ')
        sGPA = input('Enter Student GPA: ')
        stu.update({sid:{'Name':sname, 'Major':smajor, 'Year':syear, 'Credit':scredit, 'GPA':sGPA}})

    elif choice=="2":
        rem = input("Enter Student ID you would like to remove: ")
        if rem in stu:
            del stu[rem]

    elif choice=="3":
        changeKey = input("Please Enter the Key you would like to change: ")
        changeVal = input(f"Please Enter the new value for {changeKey}")
        stu[changeKey] = changeVal

    elif choice=="4":
        for stuRec in stu.items():
            print(stuRec)
            print('-----------------------------------------------------------------------')

    elif choice=="5":
        break

    else:
        print("Invalid Choice")
