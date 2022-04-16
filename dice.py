import random
while True:
    percent = int(input("Enter a win chance %: "))
    numberOfRounds = int(input("Enter the number of rounds wanted to play: "))
    stateOfGame = False
    rounds = []
    resultOfRounds = []
    countWon= 0
    countLost= 0

    for i in range(numberOfRounds):
        result = random.randint(0, 100)
        if result < percent:
            stateOfGame = True
            rounds.append(stateOfGame)
            resultOfRounds.append(result)
        else:
            stateOfGame = False
            rounds.append(stateOfGame)
            resultOfRounds.append(result)

    for elem in rounds:
        if elem == False:
            countLost += 1
            continue
        if elem == True:
            countWon += 1
            continue




    print('\n')
    print("With a Win Chance of " + str(percent))
    print('You won ' + str(countWon) + ' rounds!')
    print('You lost ' + str(countLost) + ' rounds!')


    

