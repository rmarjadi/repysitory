#Riza Marjadi
"""Assignment 2-Problem 5: Caesar cipher
Cipher a string using Caesar cipher"""

def cipherCaesar(s):
    cCaesar=[]

    for c in s:
        cCaesar.append(chr(ord(c)+3))

    print('The ciphered string is: ' + ''.join(cCaesar))

more="y"
while more=="y":
    s = input('Enter a string: ')
    cipherCaesar(s)
    more=str(input("\nDo you want to cipher more? (y/n): "))
