import pickle

class Customer:
    def __init__(self, ID, name, accNum, email, balance):
        self.ID = ID
        self.name = name
        self.accNum = accNum
        self.email = email
        self.balance = balance
        self.cardsOwned = []

    def __str__(self):
        cardsInfo = '\n'.join(str(card) for card in self.cardsOwned) if self.cardsOwned else "None"
        return (
            f'ID: {self.ID} | Account Number: {self.accNum}\n'
            f'{self.name} <{self.email}>\n'
            f'${self.balance:,.2f}\n'
            f'Cards on File:\n{cardsInfo}'
        )

    def TransferTo(self, amount, customer):
        if (self.balance - amount) >= 0:
            self.balance -= amount
            customer.balance += amount
            print(f'{self.name} Transferred ${amount:,.2f} to {customer.name}.')
        else:
            print('Insufficient Funds.')

    def assignCard(self, card):
        self.cardsOwned.append(card)
        print(f'{card} assigned to {self.name}.')

class Card:
    def __init__(self, type, cardNum, cvv, expiration):
        self.type = type
        self.cardNum = cardNum
        self.cvv = cvv
        self.expiration = expiration
        self.balance = 0.0

    def __str__(self):
        return f'{self.type}\n{self.cardNum}\n{self.cvv}\n{self.expiration}\n${self.balance:,.2f}'

exampleCust1 = Customer('001', 'Kyler Dunn', '98234234', 'kbdunnvilla@gmail.com', 10378)
exampleCust2 = Customer('002', 'John Cena', '751462763', 'JohnCena@gmail.com', 5900)

exampleCard1 = Card('Credit', '1234 5678 1234 5678', '123', '01/29')
exampleCard2 = Card('Debit', '9876 5432 9876 5432', '321', '11/27')

cards = []
customers = []

customers.append(exampleCust1)
customers.append(exampleCust2)
cards.append(exampleCard1)
cards.append(exampleCard2)

while True:
    print('1. Add Customer')
    print('2. Add Card')
    print('3. Transfer Funds')
    print('4. Assign Card')
    print('5. Display Customer Information')
    print('6. Display Card Information')
    print('7. Commit')
    print('8. Quit')
    choice = input('Select an Option: ')
    if choice=='1':
        ID = input('Please Enter ID: ')
        name = input('Please Enter Name: ')
        accNum = input('Please Enter Account Number: ')
        email = input('Please Enter Email: ')
        balance = float(input('Please Enter Balance: '))
        newCustomer = Customer(ID, name, accNum, email, balance)
        customers.append(newCustomer)
        print('Customer Added!')
    elif choice=='2':
        type = input('Debit or Credit? ')
        cardNum = input('Enter Card Number: ')
        cvv = input('Enter CVV: ')
        expiration = input('Enter Expiration (MM/YY):')
        newCard = Card(type, cardNum, cvv, expiration)
        cards.append(newCard)
    elif choice=='3':
        if len(customers) >= 2:
            amount = float(input('Enter Amount Transferred: $'))
            i=1
            for Customer in customers:
                print(f'[{i}] {Customer}')
                i+=1
            choice1 = int(input('Select Customer Transferring: ')) - 1
            choice2 = int(input('Select Customer Transferred To: ')) - 1
            (customers[choice1]).TransferTo(amount, (customers[choice2]))
        else:
            print('Not Enough Customers.')
    elif choice=='4':
        if len(customers) > 0 and len(cards) > 0:
            i=1
            for Customer in customers:
                print(f'[{i}] {Customer}')
                i+=1
            choice1 = int(input('Select Customer: ')) - 1
            i=1
            for Card in cards:
                print(f'[{i}] {Card}')
                i+=1
            choice2 = int(input('Select Card:')) - 1
            (customers[choice1]).assignCard(cards[choice2])
        else:
            print('Invalid Number of Cards or Customers.')
    elif choice=='5':
        print('')
        for customer in customers:
            print(f'{customer}\n')
    elif choice=='6':
        print('')
        for card in cards:
            print(f'{card}\n')
    elif choice == '7':
        with open('bankInfo.dat', 'wb') as file:
            pickle.dump((customers, cards), file)
        print("Commit Complete.")
    elif choice=='8':
        break
    else:
        print('Invalid Option.')
