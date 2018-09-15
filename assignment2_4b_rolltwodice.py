#Riza Marjadi
"""Assignment 2-Problem 4b: Two-dice roll
Simulate rolls of two dice and log the outcomes"""

import random

print('This program will simulate rolling of two dice and keep the log of outcomes\n')

def rollTwoDice():
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    roll = die1 + die2
    return (die1, die2, roll)

more='y'
rollno = 0
rolllog = {2:0, 3:0, 4:0, 5:0, 6:0, 7:0,
           8:0, 9:0, 10:0, 11:0, 12:0}

while more=='y':
    rollno += 1
    thisroll=rollTwoDice()

    rolllog[thisroll[2]] = rolllog[thisroll[2]] + 1

    print('=' * 25 + '\n')
    print('Number of rolls: ' + str(rollno))
    print('Die 1 shows: ' + str(thisroll[0]))
    print('Die 2 shows: ' + str(thisroll[1]))
    print('Outcome for this roll: ' + str(thisroll[2]) +'\n')
    print('Outcomes'.center(11) + 'Frequencies'.center(11))
    
    for outcome in rolllog:
        print(str(outcome).center(10) + str(rolllog[outcome]).center(11))
    
    more=input('Roll again? (y/n): ')
    
