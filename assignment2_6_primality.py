#Riza Marjadi
"""Assignment2-Problem 6: Check primality of an integer"""

print('This program will check if a positive integer is a prime number.')

def isPrime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False

    i=5
    while i**2 <= n:
        if n % i == 0 or n % (1+2) == 0:
            return False
        i += 6

    return True

more="y"
while more=="y":
    n=int(input('Enter an integer: '))

    if isPrime(n):
        print('It is a prime number.')
    else:
        print('It is not a prime number.')
        
    more=str(input("\nDo you want to try again? (y/n): "))
      
