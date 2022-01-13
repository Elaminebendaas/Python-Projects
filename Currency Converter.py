from currency_converter import CurrencyConverter
import os
import time
c = CurrencyConverter()
file = open('exchange.txt', 'w')



def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

def main():
    time.sleep(1)
    print('===========================================================')
    time.sleep(1)
    print('1. Currency conversion')
    time.sleep(2)
    print('2. 1:1 value of currencies')
    time.sleep(2)
    print('3. Enter a specific date and view the value of the conversion during that day ')
    time.sleep(0.5)
    print('If you would like to exit enter 4!')
    time.sleep(0.5)
    print('===========================================================')

    user_selection = float(input('Please select a choice between 1-3'))

    if user_selection == 1:
        currency_1 = input("Please enter the original currency(ex: USD): ").upper()
        currency_1.strip()
        currency_2 = input('Enter the currency you would like to convert to(ex: CAD): ').upper()
        currency_2.strip()
        amount = float(input('Enter the amount you would like to convert: '))
        conversion(currency_1, currency_2, amount)

    if user_selection == 2:
        currency_1 = input("Please enter the original currency(ex: USD): ").upper()
        currency_1.strip()
        currency_2 = input('Enter the currency you would like to convert to(ex: CAD): ').upper()
        currency_2.strip()
        values(currency_1, currency_2)
    
    if user_selection == 4:
        exit()

def conversion(currency_1, currency_2, amount):
    conversion = c.convert(amount, currency_1, currency_2)
    clearConsole()
    print(f'{amount} of {currency_1} converts to {conversion} in {currency_2}')
    file.write(f'{amount} of {currency_1} converts to {conversion} in {currency_2}')
    time.sleep(1.5)
    main()

def values(currency_1, currency_2):
    conversion = c.convert(1, currency_1, currency_2)
    clearConsole()
    print(f'1 {currency_1} is worth {currency_2}')
    file.write(f'1 {currency_1} is worth {conversion}{currency_2}')
    time.sleep(1.5)
    main()




while True:
    main()









