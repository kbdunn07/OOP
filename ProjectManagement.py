managers=[]
technologies=[]
teamMembers=[]

Projects = {"p1":
                {
                'Project Title': "Project Test",
                'Managers':managers,
                'Start Date':"Sep 22nd, 2025",
                'End Date':"October 1st, 2025",
                'Sponsor':"John",
                'Budget':1000,
                'Technologies':technologies,
                'Team Members':teamMembers
                }
            }
while True:
    print("\n1. Project Initiation\n2. Project Closure\n3. Project Progress Update\n4. Print Projects\n5. Quit Application")
    choice = input("\nPlease Select an Option:\n")
    if choice =='1':
        ID = input("\nPlease Enter Project ID: ")
        title = input('\nPlease Enter Project Title: ')
        print('\nEnter Manager Names (Type DONE when finished):\n')
        while True:
            names = input('\nEnter Manager: ')
            if names.upper()=='DONE':
                break
            managers.append(names)
        startDate = input('\nPlease Enter Starting Date: ')
        endDate = input('\nPlease Enter End Date: ')
        sponsor = input('\nPlease Enter Sponsor: ')
        budget = input('\nPlease Enter Budget: ')
        print('\nEnter Technologies (Type DONE when finished):\n')
        while True:
            tech = input('\nEnter Technology: ')
            if tech.upper()=='DONE':
                break
            technologies.append(tech)
        print('\nEnter Team Members (Type DONE when finished):\n')
        while True:
            team = input('\nEnter Team Member: ')
            if team.upper()=='DONE':
                break
            teamMembers.append(team)
        Projects.update({ID:{'Project Title':title, 'Managers':managers, 'Start Date':startDate, 'End Date':endDate, 'Sponsor':sponsor, 'Budget':budget, 'Technologies':technologies, 'Team Members':teamMembers}})

    elif choice == '2':
        option = input("\nEnter Project ID: ")
        if option in Projects:
            del Projects[option]
        else:
            print("\nInvalid ID\n")

    elif choice =='3':
        major = input('\nEnter ID of Project being Updated: ')
        if major in Projects:
            minor = input('\nEnter Field being Updated: ')
            if minor in Projects[major]:
                if minor=="Managers":
                    new = input("\nPlease Provide Manager Name: ")
                    Projects[major][minor].append(new)
                elif minor=="Technologies":
                    new = input('\nPlease Enter Technology: ')
                    Projects[major][minor].append(new)
                elif minor=="Team Members":
                    new = input('\nPlease Enter Member: ')
                    Projects[major][minor].append(new)
                else:
                    new = input('\nPlease Provide New Value: ')
                    Projects[major][minor] = new
            else:
                print('\nInvalid Field\n')
        else:
            print('\nInvalid ID\n')


    elif choice =='4':
        for printAll in Projects.items():
            print(*printAll)
            print('-----------------------------------------------------------------------')

    elif choice =='5':
        break
