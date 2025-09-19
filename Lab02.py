myEmployees = {}

while True:
    print('\n'
          '1. Add Employee\n'
          '2. Delete Employee\n'
          '3. Modify Employee\n'
          '4. Display Employees\n'
          '5. Quit')
    choice = input("\nPlease Select an option: ")

    if choice == '1':
        name = input("\nPlease Enter Employee Name: ")
        basicPay = int(input('\nPlease Enter Employee Basic Pay: '))
        allowance = int(input('\nPlease Enter Employee Allowance: '))
        deductions = int(input('\nPlease Enter Employee Deductions: '))
        taxes = int(input('\nPlease Enter Employee Taxes: '))
        netPay = basicPay+allowance
        grossPay = netPay - (deductions+taxes)
        myEmployees.update({name:{'Basic Pay':basicPay, 'Allowance':allowance, 'Deductions':deductions, 'Taxes':taxes, 'Net Pay':netPay, 'Gross Pay':grossPay}})

    elif choice == '2':
        option = input('\nWhat is the name of the Employee you would like to remove?\n')
        if option in myEmployees:
            del myEmployees[option]
        else:
            print('Invalid Employee')

    elif choice == '3':
        major = input('\nWhat is the name of the Employee you would like to change?\n')
        if major in myEmployees:
            minor = input(f'\nWhat would you like to change about {major}? (Basic Pay, Allowance, Deductions, Taxes)\n')
            if minor in myEmployees[major]:
                new = input('Please Enter new Value: ')
                myEmployees[major][minor] = new
                if minor =='Allowance':
                    netPay = basicPay + int(new)
                    grossPay = netPay - (deductions + taxes)
                elif minor =='Basic Pay':
                    netPay = int(new) + allowance
                    grossPay = netPay - (deductions + taxes)
                elif minor == 'Deductions':
                    grossPay = netPay - (int(new) + taxes)
                elif minor == 'Taxes':
                    grossPay = netPay - (deductions + int(new))
                myEmployees[major]['Net Pay'] = netPay
                myEmployees[major]['Gross Pay'] = grossPay
            else:
                print('Invalid option\n')

    elif choice == '4':
        for empRec in myEmployees.items():
            print(*empRec)
            print('-----------------------------------------------------------------------')

    elif choice == '5':
        break

    else:
        print('Invalid Choice')