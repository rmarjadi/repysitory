#Riza Marjadi
"""Assignment 2-Problem 1: Isogram
Check if a word is an isogram --- a word in which
no letter of the alphabet appears more than once."""

print('This program will determine if a word is an isogram - no letter of the alphabet appears more than once.\n')


def isogram(inputText):
    count= {}
    isogram = True

    for character in inputText:
        count.setdefault(character, 0)
        count[character] = count[character] + 1
        if count[character] > 1:
            isogram = False
            break

    if isogram:
        print('The word "' + inputText + '" is an isogram.\n')
    else:
        print('The word "' + inputText + '" is not an isogram.\n')

while True:
    inputText=input('Enter a word to check for isogram (enter "n" to stop): ')
    if inputText=='n':
        break
    else:
        isogram(inputText)
        
    
