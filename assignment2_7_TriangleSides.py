#Riza Marjadi
"""Assignment 2-Problem 7: Check if three sides can form a triangle
"""
print('This program will check if the lengths of three sides can form a triangle.\n')

def checkTriangleSides():
    sides=[]

    for side in range(3):
        s=float(input('Enter the length of side no. ' + str(side+1) + ': '))
        sides.append(s)

    sides.sort()

    if sides[0]+sides[1] > sides[2]:
        print('The sides with those lengths can form a triangle.')
    else:
        print('The sides with those lengths cannot form a triangle.')

more='y'
while more=="y":
    checkTriangleSides()
    more=str(input("\nDo you want to try again? (y/n): "))
