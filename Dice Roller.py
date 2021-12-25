#This code will allow you to roll 1-2 dice
#A dice that's has 1-6
#Exception catching is present in this code

import random


def roll_die():
    
    while True:
        try:
            n = float(input("How many dice would you like to roll between 1 and 2: "))
            if n == 1:
                print(random.randrange(1, 6))
            elif n == 2:
                print(random.randrange(1, 6))
                print(random.randrange(1, 6))
            else:
                n = input("Please enter a digit between 1-2!: ")
        except ValueError:
            n = input("Please enter a number! (Between 1-2): ")
        
  




roll_die()



            