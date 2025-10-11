
class Book:
    def __init__(self, book_id, book_title, author=None, publisher=None, year=None):
        self.book_id = book_id
        self.book_title = book_title
        self.author = author
        self.publisher = publisher
        self.year = year

    def display(self):
        print(f"\nID: {self.book_id}")
        print(f'Title: {self.book_title}')
        print(f'Author: {self.author}')
        print(f'Publisher: {self.publisher}')
        print(f'Published in {self.year}')

    def __str__(self):
        return f'[{self.book_id}] {self.book_title} written by {self.author}, published by {self.publisher} in {self.year}'


class Author:
    def __init__(self, author_id, author_name, affiliation, country, phone, email):
        self.author_id = author_id
        self.author_name = author_name
        self.affiliation = affiliation
        self.country = country
        self.phone = phone
        self.email = email

    def getPublisher(self):
        return self.affiliation

    def __str__(self):
        return f'[{self.author_id}] {self.author_name} affiliated with {self.affiliation} from {self.country} <{self.email}> <{self.phone}>'


class User:

    def __init__(self, userID, userName, email, password, address, phone):
        self.userID = userID
        self.userName = userName
        self.password = password
        self.address = address
        self.phone = phone
        self.email = email
        self.booksBorrowed = []

    def borrowBook(self, book):
        self.booksBorrowed.append(book)

    def displayBooks(self):
        print('Books Borrowed: ')
        for items in self.booksBorrowed:
            print(items)

    def display(self):
        print(f'\nUser ID: {self.userID}')
        print(f'User Name: {self.userName}')
        self.displayBooks()

    def __str__(self):
        return f'[{self.userID}] {self.userName} <{self.email}> <{self.phone}>'


allAuthors = []
allBooks = []
allUsers = []

while True:
    print("\nWelcome to my Library!")
    print('1. Add Book')
    print('2. Add Author')
    print('3. Add User')
    print('4. Borrow Book')
    print('5. Display')
    print('6. Quit\n')
    choice = input('Select an Option: ')

    if choice == '1':
        bookID = input('Enter Book ID: ')
        bookTitle = input('Enter Book Title: ')
        publishYear = input('Enter Year Published: ')
        if allAuthors:
            print('Available Authors: ')
            startNum = 1
            for i in allAuthors:
                print(f'\n({startNum}) {i}')
                startNum += 1
            choice = input('Select an Author: ')
            if choice:
                author = allAuthors[int(choice) - 1]
            else:
                author = None
        else:
            author = None
            print('No Available Authors')

        if author:
            myBook = Book(bookID, bookTitle, author, author.getPublisher(), publishYear)
        else:
            myBook = Book(bookID, bookTitle, author, None, publishYear)
        allBooks.append(myBook)

    elif choice == '2':
        authorID = input('Author ID: ')
        authorName = input('Author Name: ')
        authorAffiliation = input('Author Affiliation: ')
        authorCountry = input('Author Country: ')
        authorPhone = input('Author Phone Number: ')
        authorEmail = input('Author Email Address: ')
        myAuthor = Author(authorID, authorName, authorAffiliation, authorCountry, authorPhone, authorEmail)
        allAuthors.append(myAuthor)

    elif choice == '3':
        user_id = input('User ID: ')
        user_name = input('User Name: ')
        user_email = input('User Email: ')
        user_password = input('User Password: ')
        user_address = input('User Address: ')
        user_phone = input('User Phone Number: ')
        myUser = User(user_id, user_name, user_email, user_password, user_address, user_phone)
        allUsers.append(myUser)

    elif choice == '4':
        print('Which User?: ')
        startNum = 1
        for i in allUsers:
            print(f'\n({startNum}) {i}')
            startNum += 1
        choice = input('Select User: ')
        if choice:
            currentUser = allUsers[int(choice) - 1]
            print('Available Books: ')
            startNum = 1
            for i in allBooks:
                print(f'\n({startNum}) {i}')
                startNum += 1
            choice = input('Select a Book to Borrow: ')
            currentUser.borrowBook(allBooks[int(choice) - 1])
            print(f'{currentUser} borrowed {allBooks[int(choice) - 1]}')
        else:
            print('Invalid User')

    elif choice=='5':
        print('1. Display Books')
        print('2. Display Authors')
        print('3. Display Users')
        choice = input('Select an Option: ')
        if choice=='1':
            if not allBooks:
                print('No Books Available')
            else:
                for i in allBooks:
                    print(i)
        elif choice=='2':
            if not allAuthors:
                print('No Available Authors')
            else:
                for i in allAuthors:
                    print(i)
        elif choice=='3':
            if not allUsers:
                print('No Available Users')
            else:
                for i in allUsers:
                    print(i)
                    i.displayBooks()
        else:
            print('Invalid Option')

    elif choice == '6':
        break

    else:
        print('Invalid Option')