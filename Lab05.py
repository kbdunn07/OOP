import tkinter as tk
from tkinter import ttk

class Stack:
    def __init__(self):
        self.element = []

    def push(self):
        self.element.append(getEntryS())
        outputTextbox.insert(tk.END, getEntryS() + ' Added to Stack!\n')
        pushEntry.delete(0, tk.END)


    def pop(self):
        outputTextbox.insert(tk.END, self.element[len(self.element) - 1] + ' Removed from Stack!\n')
        self.element.pop(len(self.element) - 1)


    def displayStack(self):
        print('Elements in Stack: ')
        outputTextbox.insert(tk.END, 'Elements in Stack:\n')
        for i in self.element:
            print(i)
            outputTextbox.insert(tk.END, (i+'\n'))

class Queue:
    def __init__(self):
        self.element = []

    def enqueue(self):
        self.element.append(getEntryQ())
        outputTextbox.insert(tk.END, getEntryQ() + ' Added to Queue!\n')
        enEntry.delete(0, tk.END)


    def dequeue(self):
        outputTextbox.insert(tk.END, self.element[0] + ' Removed from Queue!\n')
        self.element.pop(0)


    def displayQueue(self):
        print('Elements in Queue: ')
        outputTextbox.insert(tk.END, 'Elements in Queue:\n')
        for i in self.element:
            print(i)
            outputTextbox.insert(tk.END, (i + '\n'))
q1 = Queue()
window = tk.Tk()

window.title('Queue/Stack Application')
window.geometry('600x600')
#ENQ Entry
enQVAR = tk.StringVar()
def getEntryQ():
    entry = enQVAR.get()
    return entry
enEntry = tk.Entry(window, textvariable=enQVAR, width=20, font=('calibre',16,'normal'))
enEntry.grid(row=2, column=2, padx=10)

enQ = tk.Button(window, text='Enqueue', width=15, height=2, bg='#E8DCA0', command=q1.enqueue)
deQ = tk.Button(window, text='Dequeue', width=15, height=2, bg='#E8DCA0', command=q1.dequeue)
displayQ = tk.Button(window, text='Display Queue', width=15, height=2, bg='#E8DCA0', command=q1.displayQueue)

enQ.grid(row=2, column=1, padx=10, pady=5)
deQ.grid(row=3, column=1, padx=10, pady=5)
displayQ.grid(row=4, column=1, padx=10, pady=5)

s1 = Stack()

pushVAR = tk.StringVar()
def getEntryS():
    entry = pushVAR.get()
    return entry
pushEntry = tk.Entry(window, textvariable=pushVAR, width=20, font=('calibre',16,'normal'))
pushEntry.grid(row=5, column=2, padx=10)

outputTextbox = tk.Text(window, height=30, width=50)
outputTextbox.place(y=320, x=100)

push = tk.Button(window, text='Push', width=15, height=2, bg='#E8DCA0', command=s1.push)
pop = tk.Button(window, text='Pop', width=15, height=2, bg='#E8DCA0', command=s1.pop)
displayS = tk.Button(window, text='Display Stack', width=15, height=2, bg='#E8DCA0', command=s1.displayStack)

push.grid(row=5, column=1, padx=10, pady=5)
pop.grid(row=6, column=1, padx=10, pady=5)
displayS.grid(row=7, column=1, padx=10, pady=5)

window.mainloop()
