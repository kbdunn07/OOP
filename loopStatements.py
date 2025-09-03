'''
Problem 1:
for i in range(1,20):
    if (i % 2 == 0):
        print(f'{i} EVEN')
    else:
        print(f'{i} ODD')

Problem 2:
num = int(input('Please enter a Number: '))
for i in range(1,10):
    print(f'{i} x {num} = {(i*num)}\n')
'''


p= int(input("Enter the Loan Amount : $"))
R = int(input("Enter the interest rate: %"))
n = int(input("Enter the Term: "))
r = R/(n*100)
EMI = p * r * ((1+r)**n) / ((1+r)**n - 1)
balance = p
for i in range(1,n+1):
    balance -= EMI
    print(f"EMI = {EMI}\nBalance = {(balance)}\n-----")

