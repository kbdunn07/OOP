class Book:
    def __init__(self):
        self.book_id = ""
        self.book_title = ""
        self.author = ""
        self.publisher = ""
        self.year = ""

    def book(self, author):
        self.book_id = input('\nEnter Book ID: ')
        self.book_title = input('Enter Book Title: ')
        self.author = author
        self.publisher = author.getPublisher()
        self.year = input('Enter Year Published: ')

    def display(self):
            print(f"\nID: {self.book_id}")
            print(f'Title: {self.book_title}')
            print(f'Author: {self.author}')
            print(f'Publisher: {self.publisher}')
            print(f'Published in {self.year}')

    def __str__(self):
        return f'{self.book_title} by {self.author}'

class Author:
    def __init__(self):
        self.author_id = ""
        self.author_name = ""
        self.affiliation = ""
        self.country = ""
        self.phone = ""
        self.email = ""

    def addAuthor(self):
        self.author_id = input('\nEnter Author ID: ')
        self.author_name = input('Enter Author Name: ')
        self.affiliation = input('Enter Affiliation: ')
        self.country = input('Enter Country: ')
        self.phone = input('Enter Phone Number: ')
        self.email = input('Enter Email: ')

    def getPublisher(self):
        return self.affiliation

    def __str__(self):
        return f'{self.author_name} affiliated with {self.affiliation}'


class User:

    def __init__(self):
        self.userID = ""
        self.userName = ""
        self.password = ""
        self.address = ""
        self.phone = ""
        self.email = ""
        self.booksBorrowed = []

    def addUser(self):
        self.userID = input("\nEnter User ID: ")
        self.userName = input('Enter User Name: ')
        self.email = input('Enter Email: ')
        self.password = input('Enter Password: ')
        self.address = input('Enter Address: ')
        self.phone = input('Enter Phone Number: ')

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

author1 = Author()
author1.addAuthor()
book1 = Book()
book1.book(author1)
book1.display()