list = []

while True:
    print('1. Add an Element to the list\n2. Remove an Element from the list\n3. Replace an Element in the list\n4. Sort the Elements in the list\n5. Reverse the Elements in the list\n6. Print the list Elements\n7. Exit')
    option = input("Please Enter your choice: ")
    if option=="1":
        var = input('Please enter the Element you would like to add: ')
        list.append(var)
    elif option=='2':
        var = input("Please enter the Element you would like to remove: ")
        if var in list:
            list.remove(var)
        else:
            print(f'{var} not found in List\n')
    elif option=='3':
        ind = int(input("What is the index of the element you would like to replace? "))
        if len(list) > ind and ind>=0:
            new = input("Please provide the new Element: ")
            list[ind] = new
        else:
            print('Index not in range\n')
    elif option=='4':
        list.sort()
    elif option=='5':
        list.reverse()
    elif option=='6':
        print(*list, sep='\n')
    else:
        break