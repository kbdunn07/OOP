class Car:
    def __init__(self, make, model, year, color, price, repBool, count=1):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.price = price
        self.repBool = repBool
        self.count = count

    def __str__(self):
        return f'{self.year} {self.make} {self.model} ({self.color}) | ${self.price:,.2f} | Requires Repairs: {self.repBool} | Count: {self.count}'


class Inventory:
    def __init__(self):
        self.cars = []
        self.sales = []

    def addCar(self, make, model, year, color, price, repBool, count):

        for car in self.cars:
            if (car.make == make and car.model == model and
                car.year == year and car.color == color and car.price == price and car.repBool == repBool):
                car.count += count
                print(f'Updated {make} {model} inventory by +{count}.')
                return

        newCar = Car(make, model, year, color, price, repBool, count)
        self.cars.append(newCar)
        print(f'Added {count} Car(s): {color} {year} {make} {model} | ${price:,.2f} | Requires Repairs: {repBool}')

    def displayInv(self):
        print('\nCurrent Inventory:')
        if not self.cars:
            print('No cars in inventory.')
        else:
            for i, car in enumerate(self.cars, start=1):
                print(f'({i}) {car}')
        print()

    def sell(self, index, count):
        if 0 <= index < len(self.cars):
            car = self.cars[index]
            if car.count >= count:
                totalPrice = car.price * count
                print(f'Sold {count} {car.make} {car.model}(s) for ${totalPrice:,.2f}')
                self.sales.append(f"{car.year} {car.make} {car.model} ({car.color}) for ${car.price:,.2f}")
                self.cars.remove(car)
                return totalPrice
            else:
                print('Invalid number of vehicles in stock.')
                return 0
        else:
            print('Invalid car selection.')
            return 0


class DealershipOOP:
    def __init__(self):
        self.inventory = Inventory()
        self.totalSales = 0

    def menu(self):
        while True:
            print('\n1. Add Car to Inventory\n'
                    '2. Show Inventory\n'
                    '3. Sell a Car\n'
                    '4. Show Sales\n'
                    '5. Quit\n')
            choice = input('Choose option: ')

            if choice == '1':
                make = input('Make: ')
                model = input('Model: ')
                year = input('Year: ')
                color = input('Color: ')
                price = float(input('Price: '))
                ynRep = input('Requires Repairs? (Y/N) ')
                if ynRep.upper() == 'Y':
                    repBool = True
                else:
                    repBool = False
                Count = int(input('Count: '))
                self.inventory.addCar(make, model, year, color, price, repBool, Count)

            elif choice == '2':
                self.inventory.displayInv()

            elif choice == '3':
                self.inventory.displayInv()
                if not self.inventory.cars:
                    continue
                index = int(input('Select which car you would like to sell: ')) - 1
                sale = self.inventory.sell(index, 1)
                self.totalSales += sale

            elif choice == '4':
                for sales in self.inventory.sales:
                    print(sales)
                print(f'\nTotal Sales so far: ${self.totalSales:,.2f}\n')

            elif choice == '5':
                break

            else:
                print('Invalid choice.\n')

app = DealershipOOP()
app.menu()