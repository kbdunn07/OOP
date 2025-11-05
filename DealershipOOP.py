import tkinter as tk
from sndhdr import whathdr
from tkinter import ttk

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

app=DealershipOOP()

def main():
    root = tk.Tk()
    root.title('Dealership Application')
    root.geometry('600x600')

    notebook = ttk.Notebook(root)
    notebook.pack(expand=True, fill='both')

    # Frame Creation:
    AddFrame = tk.Frame(notebook, width=500, height=500)
    InventoryFrame = tk.Frame(notebook, width=500, height=500)
    SellFrame = tk.Frame(notebook, width=500, height=500)
    SalesFrame = tk.Frame(notebook, width=500, height=500)
    SearchFrame = tk.Frame(notebook, width=500, height=500)

    AddFrame.pack()
    InventoryFrame.pack()
    SellFrame.pack()
    SalesFrame.pack()
    SearchFrame.pack()

    notebook.add(AddFrame, text='Add Car')
    notebook.add(InventoryFrame, text='Inventory')
    notebook.add(SellFrame, text='Sell Car')
    notebook.add(SalesFrame, text='Sales History')
    notebook.add(SearchFrame, text='Search Car')

#<--------------------Add Car Frame------------------>:
    makeVar=tk.StringVar()
    modelVar=tk.StringVar()
    yearVar=tk.StringVar()
    colorVar=tk.StringVar()
    priceVar=tk.StringVar()
    repairCheck = tk.IntVar()

    def submit():
        if repairCheck.get() == 1:
            repBool = True
        else:
            repBool = False
        make=makeVar.get()
        model=modelVar.get()
        year=yearVar.get()
        color=colorVar.get()
        price=float(priceVar.get())
        app.inventory.addCar(make, model, year, color, price, repBool, 1)

    makeLabel = tk.Label(AddFrame, text='Make: ', font=('calibre',10,'bold'))
    makeEntry = tk.Entry(AddFrame, textvariable= makeVar, font=('calibre',10,'normal'))

    modelLabel = tk.Label(AddFrame, text='Model: ', font=('calibre', 10, 'bold'))
    modelEntry = tk.Entry(AddFrame, textvariable=modelVar, font=('calibre', 10, 'normal'))

    yearLabel = tk.Label(AddFrame, text='Year: ', font=('calibre',10,'bold'))
    yearEntry = tk.Entry(AddFrame, textvariable= yearVar, font=('calibre',10,'normal'))

    colorLabel = tk.Label(AddFrame, text='Color: ', font=('calibre',10,'bold'))
    colorEntry = tk.Entry(AddFrame, textvariable= colorVar, font=('calibre',10,'normal'))

    priceLabel = tk.Label(AddFrame, text='Price: $', font=('calibre',10,'bold'))
    priceEntry = tk.Entry(AddFrame, textvariable= priceVar, font=('calibre',10,'normal'))

    #repairLabel = tk.Label(AddFrame, text='Requires Repairs: ', font=('calibre',10,'bold'))
    repairCheckbox = tk.Checkbutton(AddFrame, text='Requires Repairs', variable=repairCheck)

    submitButton = tk.Button(AddFrame,text='Submit',command=submit)

    makeLabel.grid(row=1,column=4)
    makeEntry.grid(row=1, column=5)

    modelLabel.grid(row=2, column=4)
    modelEntry.grid(row=2, column=5)

    yearLabel.grid(row=3, column=4)
    yearEntry.grid(row=3, column=5)

    colorLabel.grid(row=4, column=4)
    colorEntry.grid(row=4, column=5)

    priceLabel.grid(row=5, column=4)
    priceEntry.grid(row=5, column=5)
    repairCheckbox.grid(row=6,column=5)

    submitButton.grid(row=7,column=5)

# <--------------------Inventory Frame------------------>:



    root.mainloop()
if __name__=='__main__':
    main()
