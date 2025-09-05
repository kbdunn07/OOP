while True:
    print('1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Quit')
    operator = input("Enter your Choice: ")
    if operator == "1":
        n1 = int(input("Please enter the first Integer: "))
        n2 = int(input('Please enter the second Integer: '))
        print(f'{n1} + {n2} = {n1+n2}')
    elif operator == "2":
        n1 = int(input("Please enter the first Integer: "))
        n2 = int(input('Please enter the second Integer: '))
        print(f'{n1} - {n2} = {n1 - n2}')
    elif operator == "3":
        n1 = int(input("Please enter the first Integer: "))
        n2 = int(input('Please enter the second Integer: '))
        print(f'{n1} * {n2} = {n1 * n2}')
    elif operator == "4":
        n1 = int(input("Please enter the first Integer: "))
        n2 = int(input('Please enter the second Integer: '))
        print(f'{n1} / {n2} = {float(n1 / n2)}')
    elif operator == "5":
        break
    else:
        print('Please enter a valid option')
print('Thank you for using this Application')