"""Coin changes
Riza Marjadi"""

print("This program will return numbers of quarters, dimes, nickels, and pennies for a dollar value")

more='y'
while more=='y':
    while True:
        try:
            amt=float(input("\nEnter the dollar value to convert: $"))
            break
        except ValueError:
            print("\nInvalid value! Please enter a numerical value.")
        
    afterquarter=(amt*100)%25
    afterdime=afterquarter%10
    afternickel=afterdime%5
    print("\nNumber of quarters: " + str(int((amt*100)//25)))
    print("\nNumber of dimes: " + str(int(afterquarter//10)))
    print("\nNumber of nickels: " + str(int(afterdime//5)))
    print("\nNumber of pennies: " + str(int(afternickel)))
    more=str(input("\nDo you want to convert more distance values? (y/n): "))
