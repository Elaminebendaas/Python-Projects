import time
import random
file = open('invoice.txt', 'w')
item1Demand = 0
item2Demand = 0
item3Demand = 0
item1Demand_float = 0
item2Demand_float = 0
item3Demand_float = 0
item1Demandfinal = 0
item2Demandfinal = 0
item3Demandfinal = 0
selection = 0
discount_final = 0

def invoice():
    item1Total = item1Price*item1Demandfinal
    item2Total = item2Price*item2Demandfinal
    item3Total = item3Price*item3Demandfinal
    subtotal = item1Total + item2Total + item3Total
    
    tax = subtotal*0.13
    total = subtotal + tax
    discount = random.randint(1,100)
    if discount <= 60:
        discount_final = 0.1
    elif 60 < discount <= 90:
        discount_final = 0.25
    elif discount > 90:
        discount_final = 0.5

    subtotal_discount = (item1Total + item2Total + item3Total)*(1 + discount_final)
    discount_reduction = subtotal_discount*discount_final

    
    print("Here is your invoice")
    print("You got lucky and qualified for a " + str(discount_final*100) + '% discount' )
    print("=============================================")
    print('1. ' + item1 + ' x ' + str(item1Demandfinal) + "         " + str(item1Total))
    print('2. ' + item2 + ' x ' + str(item2Demandfinal) + "         " + str(item2Total))
    print('3. ' + item3 + ' x ' + str(item3Demandfinal) + "         " + str(item3Total))
    print("------------------------------------")
    print("Subtotal:                " + str(subtotal ))
    print("Subtotal (new):          " + str(subtotal_discount ))
    print("Discount:                " + str(discount_reduction))
    print("Tax:                     " + str(tax))
    print("------------------------------------")
    print("Total:                   " + str(total))
    print('=============================================')
    print('Goodbye :)')

    file.write('\n')
    file.write('Here is your invoice\n')
    file.write("You got lucky and qualified for a " + str(discount_final*100) + '% discount\n' )
    file.write("=============================================\n")
    file.write('1. ' + item1 + ' x ' + str(item1Demandfinal) + "         " + str(item1Total) + '\n')
    file.write('2. ' + item2 + ' x ' + str(item2Demandfinal) + "         " + str(item2Total) + '\n')
    file.write('3. ' + item3 + ' x ' + str(item3Demandfinal) + "         " + str(item3Total) + '\n')
    file.write("---------------------------------------------\n")
    file.write("Subtotal:                " + str(subtotal ) + '\n')
    file.write("Subtotal (new):          " + str(subtotal_discount ) + '\n')
    file.write("Discount:                " + str(discount_reduction) + '\n')
    file.write("Tax:                     " + str(tax) + '\n')
    file.write("---------------------------------------------\n")
    file.write("Total:                   " + str(total) + '\n')
    file.write("=============================================\n")

    
userName = input("Please enter your name: ")
companyName = input("Please enter your company name: ")

print('Hey ' + userName + ' lets get your shop setup for ' + companyName)
print('\nSetup: You will be required to enter 3 different products with their pricing to be able to set up your shop!')
print('\nLets get started :) ')

print('\n---------------------------------------------')
print('      Enter the details for your shop')

item1 = input("\nEnter the name for item 1 >> ")

while True:

    item1Price = input('Input the price for the item >> ')  
    try:
        val = float(item1Price)
        if val < 0:
            item1Price = input('Price must be greater than 0. Try again >> ')
            continue
    except ValueError:
        item1Price = input('Price must be an integer. Try again >> ')
        continue
    else:
        break

while True:

    item1Stock = input('Input the stock for the item >> ')  

    try:
        val = float(item1Stock)
        if val < 0:
            item1Stock = input('Stock must be greater than 0. Try again >> ')
            continue
    except ValueError:
        item1Stock = input('Stock must be an integer. Try again >> ')
        continue
    else:
        break

item2 = input("\nEnter the name for item 2 >> ")

while True:
    item2Price = input('Input the price for the item >> ')  
    try:
        val = float(item2Price)
        if val < 0:
            item2Price = input('Price must be greater than 0. Try again >> ')
            continue
    except ValueError:
        item2Price = input('Price must be an integer. Try again >> ')
        continue
    else:
        break

while True:
    item2Stock = input('Input the stock for the item >> ')  
    try:
        val = float(item2Stock)
        if val < 0:
            item2Stock = input('Stock must be greater than 0. Try again >> ')
            continue
    except ValueError:
        item2Stock = input('Stock must be an integer. Try again >> ')
        continue
    else:
        break

item3 = input("\nEnter the name for item 3 >> ")

while True:
    item3Price = input('Input the price for the item >> ')  
    try:
        val = float(item3Price)
        if val < 0:
            item3Price = input('Price must be greater than 0. Try again >> ')
            continue
    except ValueError:
        item3Price = input('Price must be an integer. Try again >> ')
        continue
    else:
        break

while True:
    item3Stock = input('Input the stock for the item >> ')  
    try:
        val = float(item3Stock)
        if val < 0:
            item3Stock = input('Stock must be greater than 0. Try again >> ')
            continue
    except ValueError:
        item3Stock = input('Stock must be an integer. Try again >> ')
        continue
    else:
        break

item1Stock = float(item1Stock)
item1Price = float(item1Price)

item2Stock = float(item2Stock)
item2Price = float(item2Price)

item3Stock = float(item3Stock)
item3Price = float(item3Price)


print("Great everything is setup!")


print("The list is being generated.......")

time.sleep(0.5)

print("...")

time.sleep(0.5)

print("......")

time.sleep(0.5)


#Part 2 (invoice)

file.write("=============================================\n")
file.write('The items that the owner listed are shown below!\n')
file.write("1. " + item1 + ' $'+ str(item1Price) + " each, " + str(item1Stock) + " available.\n")
file.write("2. " + item2 + ' $'+ str(item2Price) + " each, " + str(item2Stock) + " available.\n")
file.write("3. " + item3 + ' $'+ str(item3Price) + " each, " + str(item3Stock) + " available.\n")
file.write("=============================================\n")

while selection != 4:
    print('------------------ Welcome ------------------')
    print("=============================================")
    print("1. " + item1 + ' $'+ str(item1Price) + " each, " + str(item1Stock) + " available.")
    print("2. " + item2 + ' $'+ str(item2Price) + " each, " + str(item2Stock) + " available.")
    print("3. " + item3 + ' $'+ str(item3Price) + " each, " + str(item3Stock) + " available.")
    print("Press 4 if you would like to calculate your invoice")
    print("=============================================")
    selection = input("Select which item you would like to purchase: ")
    
    while True:
        
        try:
            val = float(selection)
            if (1 > val > 3 ):
                selection = input("Select an item between 1-3: ")
                continue
        except ValueError:
            selection = input("Not a number! Enter a number between 1-3: ")
            continue
        else:
            break
        
    selection = float(selection)
    
    if selection == 1:
        while True:
            item1Demand = input("How many of the item selected would you like to purchase?: ")
            
            try:
                item1Demand_float = float(item1Demand)
                if item1Demand_float > item1Stock or item1Demand_float < 0:
                    item1Demand = input("Please enter a valid amount there are " + str(item1Stock) + " of the item you want to purchase: ")
                    continue
            except ValueError:
                item1Demand = input("Please enter a valid amount there are " + str(item1Stock) + " of the item you want to purchase: ")
                continue
            else:
                break

    item1Stock = item1Stock - item1Demand_float
    item1Demandfinal += item1Demand_float
    item1Demand_float = 0
    
    if selection == 2:
        while True:
            item2Demand = input("How many of the item selected would you like to purchase?: ")
            
            try:
                item2Demand_float = float(item2Demand)
                if item2Demand_float > item2Stock or item2Demand_float < 0:
                    item2Demand = input("Please enter a valid amount there are " + str(item2Stock) + " of the item you want to purchase: ")
                    continue
            except ValueError:
                item2Demand = input("Please enter a valid amount there are " + str(item2Stock) + " of the item you want to purchase: ")
                continue
            else:
                break

    
    item2Stock = item2Stock - item2Demand_float
    item2Demandfinal += item2Demand_float
    item2Demand_float = 0

    if selection == 3:
        while True:
            item3Demand = input("How many of the item selected would you like to purchase?: ")
            
            try:
                item3Demand_float = float(item3Demand)
                if item3Demand_float > item3Stock or item3Demand_float < 0:
                    item3Demand = input("Please enter a valid amount there are " + str(item3Stock) + " of the item you want to purchase: ")
                    continue
            except ValueError:
                item3Demand = input("Please enter a valid amount there are " + str(item3Stock) + " of the item you want to purchase: ")
                continue
            else:
                break
        item3Stock = item3Stock - item3Demand_float
        item3Demandfinal += item3Demand_float
        item3Demand_float = 0

exit_user = print("Press c if you would like to cancel the order. If you would like to continue press i")  

if exit_user == 'c':
    exit()

invoice()











