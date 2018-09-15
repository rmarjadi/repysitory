#Riza Marjadi
"""Assignment 2-Problem 9: List ASCII values for
a string input"""

print('This program will list the ASCII values for each letter in a string input.\n')

more="y"
while more=="y":
    s = input('Enter a string: ')

    for letter in s:
        print(letter + ' = ' + str(ord(letter)))

    more=str(input("\nDo you want to try again? (y/n): "))
