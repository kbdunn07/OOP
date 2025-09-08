list = []

while True:
    print('1. Add an Element to the List\n2. Remove a Specific Element from the List\n3. Remove/Pop an Indexed Element\n4. Display the List\n5. Quit')
    option = input("Enter your choice:\n")
    if option=="1":
        var = input("Please enter the variable you would like to add: ")
        list.append(var)
    elif option=='2':
        var = input('Please enter the element you would like to remove: ')
        if var in list:
            list.remove(var)
        else:
            print(f'{var} not found in List\n')
    elif option=='3':
        var = int(input('Please enter the index you would like removed: '))
        if len(list) > var and var>=0:
            list.pop(var)
        else:
            print("Index not in range\n")
    elif option=='4':
        print(list)
    elif option=='5':
        break
    else:
        print("Invalid Option\n")