#Riza Marjadi
"""Simulation card dealing to four sides"""

import random

def buildDeck():
    suites=['C', 'D', 'H', 'S']
    values=['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    deck=[]

    for suite in suites:
        for value in values:
            deck.append(suite+value)

    return deck
                        
def dealCards():
    deck = buildDeck()
    N=[]
    E=[]
    S=[]
    W=[]

    for i in range (0,13):
        N.append(random.choice(deck))
        deck.remove(N[i])
        E.append(random.choice(deck))
        deck.remove(E[i])
        S.append(random.choice(deck))
        deck.remove(S[i])
        W.append(random.choice(deck))
        deck.remove(W[i])

    print('North', N)
    print('East', E)
    print('South', S)
    print('West', W)
    print('\n')
    

print("This program simulates card dealing. Start the simulation by typing 'y' or stop by typing other keys.\n")
deal=input("Type 'y' to start or any other key to stop.")

while deal=='y':
    print('\n')
    dealCards()
    deal=input("Type 'y' to start or any other key to stop.")


