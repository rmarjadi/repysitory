#Riza Marjadi
"""Assignment 2-Problem 8: ASCII values for the alphabet
"""

import string

print('This program will list the ASCII values for each letter in the alphabet.\n')
def alphaASCII():
    case = input('Do you want the list for upper case or lower case? Type "A" for upper case or "a" for lower case: ')
    print('\n')

    if case == 'A':
        alphabet = list(string.ascii_uppercase)
    elif case == 'a':
        alphabet = list(string.ascii_lowercase)

    for letter in alphabet:
        print(letter + ' = ' + str(ord(letter)))

more="y"
while more=="y":
    alphaASCII()
    more=str(input("\nDo you want to run it again? (y/n): "))
