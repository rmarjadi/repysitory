"""Coin changes
Riza Marjadi"""

print("This program will return numbers of quarters, dimes, nickels, and pennies for a dollar value")

more='y'
while more=='y':
    while True:
        try:
            regularPrice=float(input("\nEnter the regular retail price: $"))
            break
        except ValueError:
            print("\nInvalid value! Please enter a numerical value.")
        
    print("\nWith 15% discount, the discounted price is: " + '${:,.2f}'.format(.85*regularPrice))
    print("\nThat is a saving of: " + '${:,.2f}'.format(.15*regularPrice))
    
    more=str(input("\nDo you want to convert more distance values? (y/n): "))
